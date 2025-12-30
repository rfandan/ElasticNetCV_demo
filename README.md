# ElasticNetCV_demo

This is a Python Machine Learning project setup using `uv` for virtual environment management, `pyproject.toml` for dependencies, and Ruff for code linting. The workflow ensures reproducibility and clean, maintainable code.

---

## Project Structure


---

## Setup and Usage Instructions

# Clone the repository
git clone <your-repo-url>
cd <your-repo-folder>

# Create and activate the virtual environment (if not created already)
uv venv                 # Create a .venv folder
source .venv/bin/activate  # Activate the virtual environment
# After this, your terminal prompt should show (.venv)

#  Install dependencies from pyproject.toml
uv install              # Reads [project.dependencies] and installs packages into .venv

#  Optional: Verify installed packages
pip list                # Should show numpy, pandas, scikit-learn, matplotlib, seaborn

#  Run your Python script
python template.py       # Inside .venv, 'python' points to the virtual environment
# Outside .venv, you may need 'python3 template.py'

#  Optional: Lint your code using Ruff
ruff check .            # Check code style and potential issues
ruff --fix .            # Automatically fix simple style issues

#  Updating dependencies
# If you add new packages to pyproject.toml:
uv install              # Installs new packages into the existing .venv
# .venv is reused; existing packages are not overwritten

#  Deactivate the virtual environment
deactivate              # Terminal returns to normal
# Reactivate later with:
source .venv/bin/activate

#  Optional: Using requirements.txt instead of pyproject.toml
# Example content of requirements.txt:
# numpy==1.25
# pandas>=2.0
# scikit-learn
# matplotlib
# seaborn
pip install -r requirements.txt  # Quick alternative to install dependencies

---

## Notes / Best Practices

# Project Name
# The 'name' in pyproject.toml does not need to match your folder; it is metadata.

# Dependency Versions
# Use safe version specifiers to prevent breaking changes:
# ^1.25 → compatible releases >=1.25.0 and <2.0.0
# >=2.0 → minimum version 2.0
# Avoid '*' unless experimenting.

# Ruff
# Ruff is an optional linter/formatter that enforces clean, readable code.
# Highly recommended for collaborative or long-term projects.

# Git
# Add '.venv/' to .gitignore so your virtual environment is not pushed to GitHub.
# Only pyproject.toml and requirements.txt should be committed for reproducibility.



1. Create new environment
    uv venv
    # or if uv command fails
    python3 -m uv venv

2. Activate environment
    source .venv/bin/activate

3. Add .venv to .gitignore
    # Python virtual environment
    .venv/

4. Create requirements.txt file

5. Install requirement file
    pip install -r requirements.txt

6. Verify installation
    pip list

7. Run your Python script
    python template.py

#Rule of thumb
    Inside .venv → use python
    Outside .venv → use python3

8. Deactivate the virtual environment
    deactivate


