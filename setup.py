"""Setup configuration for the HTTP CLI package."""

from setuptools import find_packages, setup

setup(
    name="PyFetch",
    version="1.0.0",
    packages=find_packages(include=["PyFetch", "PyFetch.*"]),  # updated packages lookup
    package_dir={"PyFetch": "PyFetch"},                       # updated package directory mapping
    install_requires=[
        "requests>=2.25.1",
    ],
    entry_points={
        "console_scripts": [
            "pyfetch=PyFetch.cli:main",
        ],
    },
    author="Malte Mindedal",
    description="A simple HTTP CLI client",
    python_requires=">=3.7",
    test_suite="tests",
)
