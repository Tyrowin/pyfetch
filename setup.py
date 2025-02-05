"""Setup configuration for the HTTP CLI package."""

from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="PyFetch",
    version="1.0.0",
    packages=find_packages(include=["PyFetch", "PyFetch.*"]),
    package_dir={"PyFetch": "PyFetch"},
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
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    license="Apache-2.0",
    test_suite="tests",
)
