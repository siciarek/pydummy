from setuptools import setup, find_packages

from tmutils import __version__

setup(
    name="tmutils",
    version=__version__,

    url="https://github.com/siciarek/pydummy.git",
    author="Jacek Siciarek",
    author_email="siciarek@gmail.com",
    install_requires=[
        "beautifulsoup4~=4.12.2",
        "python-docx~=0.8.11",
        "dependency-injector~=4.41.0",
        "Jinja2~=3.1.2",
    ],
    license="MIT",
    packages=find_packages(include=['tmutils', 'tmutils.*']),
    keywords="utils",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Silent Eight Transaction Management Team",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
)
