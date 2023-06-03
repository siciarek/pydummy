from setuptools import setup

from pydummy import __version__

setup(
    name="pydummy",
    version=__version__,

    url="https://github.com/siciarek/pydummy.git",
    author="Jacek Siciarek",
    author_email="siciarek@gmail.com",
    install_requires=[
        "beautifulsoup4",
        "python-docx",
    ],
    py_modules=[
        "pydummy"
    ],
)
