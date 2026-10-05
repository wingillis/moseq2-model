import os
import sys
import codecs
import subprocess
from setuptools import setup, find_packages


def install(package):
    subprocess.call([sys.executable, "-m", "pip", "install", package])


try:
    import numpy
except ImportError:
    install("numpy")

try:
    import future
except ImportError:
    install("future")

try:
    import six
except ImportError:
    install("six")

try:
    import cython
except ImportError:
    install("cython==0.29.14")


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), "r") as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith("__version__"):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


setup(
    name="moseq2_model",
    version=get_version("moseq2_model/__init__.py"),
    author="Datta Lab",
    description="Modeling for the best",
    packages=find_packages(exclude="docs"),
    include_package_data=True,
    platforms="any",
    python_requires=">=3.12",
    install_requires=[
        "click>=8.1",
        "cytoolz>=0.12",
        "h5py>=3.13",
        "numpy>=2.2",
        "ruamel-yaml>=0.18",
        "scipy>=1.15",
        "tqdm>=4.67",
        "pybasicbayes @ git+https://github.com/wingillis/pybasicbayes.git@master",
        "pyhsmm @ git+https://github.com/wingillis/pyhsmm.git@master",
        "autoregressive @ git+https://github.com/wingillis/pyhsmm-autoregressive.git@master",
    ],
    entry_points={"console_scripts": ["moseq2-model = moseq2_model.cli:cli"]},
)
