
import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "readme.md").read_text()

# This call to setup() does all the work
setup(
    name="cliGPT",
    version="1.0.0",
    description="Leveraging GPT in your CLI",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/kaustubh-s1/cliGPT",
    author="Kaustubh",
    author_email="shuklakaustubh84@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["cliGPT"],
    include_package_data=True,
    install_requires=["wheel", "openai", "toml", "colored", "inquirer"],
    entry_points={
        "console_scripts": [
            "cliGPT=cliGPT.__main__:main",
        ]
    },
)