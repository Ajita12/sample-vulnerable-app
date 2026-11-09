A sample repository containing intentionally insecure code and infrastructure-as-code (IaC) configurations for testing **SAST**, **SCA**, and **IaC** scanning tools

---

## Overview

This repository is designed for security testing, scanning, and training purposes. It includes:

- **SAST (Static Application Security Testing) targets:** `main.py` with hardcoded secrets, SQL injection, command injection, and insecure deserialization patterns.
- **SCA (Software Composition Analysis) targets:** `requirements.txt` with outdated and vulnerable Python dependencies.
- **IaC (Infrastructure-as-Code) targets:** `cloudformation/template.yaml` and `terraform/main.tf` containing overly permissive IAM policies, public S3 buckets, and open security groups.
- **Dockerfile:** with environment secrets, running as root, and unpinned dependencies.
- **OWASP Juice Shop (`juice-shop/`):** a full, intentionally vulnerable Node.js/TypeScript + Angular web application covering the OWASP Top 10 and beyond. Useful as a realistic target for SAST, SCA (`package.json`), container and IaC scanning, and for DAST when run locally.

> ⚠️ **Important:** Do **not** deploy these resources to production or public cloud accounts. Use in isolated test environments only.

---

## Repository Structure

```
sample-vuln-lab/
├── cloudformation/
│   └── template.yaml
├── terraform/
│   └── main.tf
├── main.py
├── requirements.txt
├── Dockerfile
├── juice-shop/          # OWASP Juice Shop v20.4.0 (vendored, MIT)
└── README.md
```

---

## Usage

1. **SAST Testing**  
   Run your static analysis tools on `main.py` to detect code issues such as hardcoded secrets, SQL injection, command injection, and insecure deserialization.

2. **SCA Testing**  
   Use dependency scanning tools against `requirements.txt` to detect outdated and vulnerable packages.

3. **IaC Testing**  
   Use IaC scanning tools on `cloudformation/template.yaml` and `terraform/main.tf` to detect misconfigurations like public S3 buckets and overly permissive IAM policies.

4. **Dockerfile Analysis**  
   Scan the Dockerfile to detect secrets in environment variables, root execution, and unpinned base images.

5. **OWASP Juice Shop**  
   Point SAST/SCA tools at `juice-shop/` (sources in `routes/`, `lib/`, `models/`, `frontend/src/`; dependencies in `package.json` and `frontend/package.json`). To run it locally for DAST or hands-on practice:
   ```bash
   # Prebuilt image
   docker run --rm -p 127.0.0.1:3000:3000 bkimminich/juice-shop:v20.4.0
   # Or from source (Node.js 22–26)
   cd juice-shop && npm install && npm start
   ```
   Then browse to http://localhost:3000. The vendored copy is the upstream [`v20.4.0`](https://github.com/juice-shop/juice-shop/tree/v20.4.0) release (commit `266448a`), unmodified, under its original MIT license (`juice-shop/LICENSE`).

---

## Notes

- All code, configurations, and Docker images are intentionally insecure for testing purposes.
- Always run in isolated or ephemeral environments.
- This repository can serve as a lab for security teams, developers learning secure coding practices, or CI/CD pipeline testing.

---

## License

This repository is provided for educational and testing purposes only. No warranty is provided. Use at your own risk.
