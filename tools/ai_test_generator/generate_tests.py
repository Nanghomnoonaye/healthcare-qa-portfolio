"""Generate pytest API test stubs from an OpenAPI spec using Claude.

For each operation in the spec, asks Claude to draft a pytest module covering
the happy path plus boundary, missing-field, and invalid-type cases for that
operation's request schema. Output is a first draft: review before wiring
into a real suite, since Claude cannot know your service's actual behaviour.

Usage:
    export ANTHROPIC_API_KEY=...
    python generate_tests.py --spec sample_openapi.yaml --output-dir generated_tests
"""
import argparse
import json
import re
from pathlib import Path

import yaml
from anthropic import Anthropic

MODEL = "claude-sonnet-5"

SYSTEM_PROMPT = """You are a senior QA automation engineer writing pytest API \
tests in Python. Given a single OpenAPI operation, output ONLY a complete, \
runnable pytest test module - no explanations, no markdown fences.

Requirements:
- Use a fixture named `api_client` (assumed to exist in conftest.py) that \
exposes `.get/.post/.put/.delete`, returning a `requests.Response`-like object.
- Cover: the happy path, each required-field-missing case, boundary values \
for any numeric field with minimum/maximum (min-1, min, max, max+1), and one \
invalid-type case per typed field.
- Use pytest.mark.parametrize where it removes duplication.
- Give every test function a one-line docstring naming what it checks.
- Assert on status_code, and on response body fields where the schema \
implies an expected shape.
"""


def load_spec(path: Path) -> dict:
    text = path.read_text()
    if path.suffix in (".yaml", ".yml"):
        return yaml.safe_load(text)
    return json.loads(text)


def iter_operations(spec: dict):
    for path, methods in spec.get("paths", {}).items():
        for method, operation in methods.items():
            if method.lower() in ("get", "post", "put", "patch", "delete"):
                yield path, method.lower(), operation


def slugify(path: str, method: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "_", path.lower()).strip("_")
    return f"test_{method}_{slug}"


def build_user_prompt(path: str, method: str, operation: dict) -> str:
    return (
        f"Endpoint: {method.upper()} {path}\n\n"
        f"OpenAPI operation object:\n{json.dumps(operation, indent=2)}"
    )


def generate_test_module(client: Anthropic, path: str, method: str, operation: dict) -> str:
    response = client.messages.create(
        model=MODEL,
        max_tokens=2000,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": build_user_prompt(path, method, operation)}],
    )
    return response.content[0].text


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--spec", required=True, type=Path)
    parser.add_argument("--output-dir", default=Path("generated_tests"), type=Path)
    args = parser.parse_args()

    spec = load_spec(args.spec)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    client = Anthropic()

    for path, method, operation in iter_operations(spec):
        slug = slugify(path, method)
        print(f"Generating {slug}...")
        code = generate_test_module(client, path, method, operation)
        (args.output_dir / f"{slug}.py").write_text(code)

    print(f"Done. Review generated tests in {args.output_dir}/ before committing.")


if __name__ == "__main__":
    main()
