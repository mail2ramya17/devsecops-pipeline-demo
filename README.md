# DevSecOps Pipeline Demo (GitHub Actions)

A tiny Flask app with a **full security pipeline** — the same gates used at
AT&T/Cisco, on free tools:

| Stage | Tool | Catches |
|---|---|---|
| Secrets | GitLeaks | hardcoded keys |
| SAST | Semgrep | code flaws (SQLi, etc.) |
| SCA | pip-audit + Dependabot | vulnerable libraries |
| Container | Trivy | image CVEs |
| DAST | OWASP ZAP baseline | runtime web issues |

Results upload to the GitHub **Security** tab (SARIF).

## Run app locally
```bash
pip install -r requirements.txt
python app.py      # http://127.0.0.1:5000
```

## Try it
1. Push → open the **Actions** tab and watch each gate.
2. Edit `app.py` to use the commented-out unsafe SQL line → push → Semgrep fails.
