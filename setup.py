import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup (
    name = "analyze_site",
    version = "0.1",
    author = "Tim Lee",
    author_email = "timhl81@gmail.com",
    description = "Utility to crawl web site looking for key words",
    license = "Apache 2.0",
    keywords = "web crawl analyze",
    url = "https://github.com/OV105/site-analyzer",
    long_description = read("README.md"),
    classifiers = [
        "Topic :: Utilities",
        "License :: OSI Approved :: Apache 2.0",
        "Development Status :: 4 Beta"
    ],
    py_modules = ["analyze_site"]

)
