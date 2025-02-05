"""Setup configuration for the HTTP CLI package."""

from setuptools import find_packages, setup

setup(
    name="PyFetch",  # Changed from http-cli
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "requests>=2.25.1",
    ],
    entry_points={
        "console_scripts": [
            "pyfetch=http_cli.cli:main",  # Changed from http_cli=http_cli.cli:main
        ],
    },
    author="Malte Mindedal",
    description="A simple HTTP CLI client",
    python_requires=">=3.7",
    test_suite="tests",
)
