"""Executa testes reais; --record salva evidências sem dados do usuário."""

import argparse
import hashlib
import io
import json
import platform
from datetime import datetime, timezone
from pathlib import Path
import unittest

from scripts.demo import demonstrate


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--record", action="store_true", help="Salvar resultados em evidence/")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    stream = io.StringIO()
    suite = unittest.defaultTestLoader.discover(str(root / "tests"))
    result = unittest.TextTestRunner(stream=stream, verbosity=2).run(suite)
    transcript = stream.getvalue()
    demo = demonstrate()
    print(transcript, end="")
    print(demo)
    if args.record:
        evidence = root / "evidence"
        evidence.mkdir(exist_ok=True)
        (evidence / "tests.txt").write_text(transcript, encoding="utf-8")
        (evidence / "demo.txt").write_text(demo + "\n", encoding="utf-8")
        sources = sorted(
            [root / "app.py"]
            + list((root / "examples").glob("*.py"))
            + list((root / "tests").glob("*.py"))
            + list((root / "scripts").glob("*.py"))
        )
        manifest = {
            "recorded_at_utc": datetime.now(timezone.utc).isoformat(),
            "python": platform.python_version(),
            "platform": platform.system(),
            "command": "python -m scripts.validate --record",
            "tests_run": result.testsRun,
            "failures": len(result.failures),
            "errors": len(result.errors),
            "success": result.wasSuccessful(),
            "scope": "SQL Injection no laboratório local; não é avaliação do Hermes/LLM",
            "sha256": {
                str(path.relative_to(root)).replace("\\", "/"):
                    hashlib.sha256(path.read_bytes()).hexdigest()
                for path in sources
            },
        }
        (evidence / "validation.json").write_text(
            json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())
