from setuptools import setup, find_packages

from tm_toolkit import __version__

setup(
    name="tm-toolkit",
    version=__version__,

    url="https://github.com/siciarek/pydummy.git",
    author="Jacek Siciarek",
    author_email="siciarek@gmail.com",
    license="MIT",
    keywords="utils",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Silent Eight Transaction Management Team",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    packages=find_packages(
        include=[
            'tm_toolkit',
            'tm_toolkit.*'
        ]
    ),
    install_requires=[
        "beautifulsoup4~=4.12.2",
        "Jinja2~=3.1.2",
        "python-docx~=0.8.11",
    ],
    entry_points={
        'console_scripts': [
            'generate-reports=tm_toolkit.entrypoints:generate_reports'
        ]
    }
)
