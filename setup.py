from setuptools import setup
import re
import os
import sys


setup(
    name="flexinet",
    version="0.0.0",
    python_requires=">3.6.0",
    author="Michael E. Vinyard - Harvard University - Massachussetts General Hospital - Broad Institute of MIT and Harvard",
    author_email="mvinyard@broadinstitute.org",
    url=None,
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    description="Flexible torch neural network architecture API",
    packages=[
        "flexinet",
    ],
    
    install_requires=[
        "numpy>=1.17.0",
        "torch>=1.10.1",
	"licorice_font>=0.0.3",
    ],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 3.6",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
    ],
    license="MIT",
)
