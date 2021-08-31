import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="eda_made_easy",
    version="1.0.0",
    description="It performs EDA within few steps",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/raghavbakshi/eda_made_easy",
    author="Raghav Bakshi",
    author_email="raghavbakshi19@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["EDA"],
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "EDA=EDA.__main__:main",
        ]
    },
)