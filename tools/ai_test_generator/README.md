# AI Test Generator

Generates pytest API test stubs from an OpenAPI spec using Claude, so the
first draft of boundary/negative-case tests doesn't have to be hand-written.

## Why

`tests/test_data_integrity.py` documents boundary-value findings (BUG-001,
BUG-002) from manually testing a numeric field. This tool automates that
style of test design: given a schema with `minimum` / `maximum` / `required`
constraints, it asks Claude to draft the boundary, missing-field, and
invalid-type cases, so a QA engineer reviews and tightens generated tests
instead of writing every case from scratch.

`sample_openapi.yaml` models a small CGM readings API with the same kind of
constraint (`value_mgdl`, min 20 / max 600) that BUG-002 was about, so the
generated tests read as a natural extension of that finding.

## Usage

```bash
pip install -r tools/ai_test_generator/requirements.txt
export ANTHROPIC_API_KEY=sk-...

python tools/ai_test_generator/generate_tests.py \
    --spec tools/ai_test_generator/sample_openapi.yaml \
    --output-dir tools/ai_test_generator/generated_tests
```

Generated files land in `generated_tests/`, one per endpoint. Review every
file before committing — treat the output as a first draft. To run them for
real, add an `api_client` fixture to a `conftest.py` that points at your
service's base URL and exposes `.get/.post/.put/.delete`.
