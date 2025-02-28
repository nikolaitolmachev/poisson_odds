from setuptools import setup
import toml


with open("pyproject.toml", "r") as f:
    config = toml.load(f)

name = config["project"]["name"]
version = config["project"]["version"]
description = config["project"]["description"]
author_name = config["project"]["authors"][0]["name"]
author_email = config["project"]["authors"][0]["email"]
homepage = config["project"]["urls"]["Homepage"]

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name=name,
    version=version,
    author=author_name,
    author_email=author_email,
    description=description,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=homepage,
    packages=['poisson_odds'],
    install_requires=['tabulate'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)