from setuptools import setup

from tm_utils import __version__

setup(
    name="tm-utils",
    version=__version__,

    url="https://github.com/siciarek/pydummy.git",
    author="Jacek Siciarek",
    author_email="siciarek@gmail.com",
    install_requires=[
        "beautifulsoup4",
        "python-docx",
    ],
    py_modules=[
        "tm-utils"
    ],
)
