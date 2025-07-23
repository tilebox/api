# /// script
# dependencies = [
#     "ruamel-yaml",
# ]
# ///

import os
import sys
from ruamel.yaml import YAML
from pathlib import Path
from typing import Dict, Any
import tempfile

override = {
    "info": {
        "title": "Tilebox API",
        "version": "1.0.0",
    },
    "servers": [
        {
            "url": "https://api.tilebox.com",
        },
    ],
    "components": {
        "schemas": {
            "connect-protocol-version": {
                "default": 1,
            },
        },
        "securitySchemes": {
            "bearerAuth": {
                "type": "http",
                "scheme": "bearer",
            },
        },
    },
    "security": [
        {
            "bearerAuth": [],
        },
    ],
}


def recursive_merge(base: Dict[Any, Any], update: Dict[Any, Any]):
    for key, value in update.items():
        if key in base and isinstance(base[key], dict) and isinstance(value, dict):
            # Both values are dictionaries, merge recursively
            recursive_merge(base[key], value)
        else:
            # Either key doesn't exist in base, or one of the values is not a dict
            base[key] = value


def main() -> None:
    output = "openapi.yaml"
    if len(sys.argv) == 2:
        output = sys.argv[1]
    elif len(sys.argv) != 1:
        print("Usage: uv run generate-openapi.py <output>")
        sys.exit(1)

    tmpdir = tempfile.TemporaryDirectory()
    print(f"Generating protobuf to {tmpdir.name}")
    os.system(f"buf generate -o {tmpdir.name}")

    yaml = YAML(typ="safe")
    yaml.default_flow_style = False

    merged_yaml = {}

    for path in Path(tmpdir.name).glob("**/*.yaml"):
        print(f"Merging {path}")

        with open(path) as f:
            data = yaml.load(f.read())
            recursive_merge(merged_yaml, data)

    recursive_merge(merged_yaml, override)

    tmpdir.cleanup()

    print(f"Writing merged output to {output}")
    with open(output, "w") as out:
        yaml.dump(merged_yaml, out)


if __name__ == "__main__":
    main()
