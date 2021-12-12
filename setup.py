import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="farsi-tokenizer",
    version="1.0.0",
    description="Read the latest Real Python tutorials",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/iamdanialkamali/farsi-tokenizer",
    author="Danial Kamali",
    author_email="kamalida@msu.edu",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=[""],
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "realpython=farsi-tokenizer.__main__:main",
        ]
    },
)