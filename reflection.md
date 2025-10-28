# Reflection on Static Code Analysis Lab

## 1️⃣ Easiest vs Hardest Issues
- **Easiest:** Fixing unused imports and spacing (Flake8) — quick edits.
- **Hardest:** Refactoring `eval()` and `open()` usage — needed deeper understanding of safe and proper coding practices.

## 2️⃣ False Positives
- Bandit flagged `try/except` blocks even after specific exceptions were used, but those were necessary for validation logic.

## 3️⃣ Integrating Tools in Workflow
- These tools can be added as **pre-commit hooks** or **GitHub Actions** so that every commit automatically checks for code quality and security issues.

## 4️⃣ Improvements Observed
- Readability improved after following PEP8 and adding docstrings.
- Code became more secure and maintainable.
- Pylint score improved from 4.8/10 to 9.8/10.

## 5️⃣ Key Takeaway
Static code analysis is like having an automated reviewer — it helps detect bugs, enforce standards, and build robust, secure Python code.
