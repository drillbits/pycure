from setuptools import setup, find_packages
import os

here = os.path.dirname(__file__)
readme = open(os.path.join(here, "README.rst")).read()

install_requires = []

setup(
    name="pycure",
    author="drillbits",
    author_email="neji@drillbits.jp",
    version="0.0.1",
    description="",
    long_description=readme,
    license="MIT License",
    test_suite="pycure",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=install_requires,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.3",
        "Topic :: Utilities",
    ],
)
