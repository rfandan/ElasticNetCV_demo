from setuptools import find_packages, setup


def read_requirements(filename: str):
    with open(filename, encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip() and not line.startswith("#")]

setup(
    name="REGRESSION_MODEL",
    version="0.0.1",
    description="Regression model using ElasticNetCV",
    author="RAJVEER FANDAN",
    author_email="dummy@example.com",
    packages=find_packages(),
    install_requires=read_requirements("requirements.txt"),
    extras_require={
        "dev": read_requirements("requirements-dev.txt")
    },
    python_requires=">=3.8",
)