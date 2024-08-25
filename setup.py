from setuptools import setup, find_packages

setup(
    name="my_autodoc",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "openai",
    ],
    entry_points={
        "console_scripts": [
            "my-autodoc=my_autodoc:main",
        ],
    },
)
