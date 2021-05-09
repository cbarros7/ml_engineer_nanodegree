from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="algebraML",
    version="0.0.5",
    author="Carlos Barros",
    author_email="cj.barros@gmail.com",
    description="This package performs basic algebraic operations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cbarros7/ml_engineer_nanodegree",
    project_urls={
        "Bug Tracker": "https://github.com/cbarros7/ml_engineer_nanodegree/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    zip_safe=False
)
