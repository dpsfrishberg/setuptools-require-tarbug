from setuptools import setup, find_packages

setup(
    name="Require Setuptools Tar Bug",
    version="1.0",
    description="Requires the setuptools tar bug", 
    author="Daniel Frishberg",
    packages=find_packages(),
    install_requires=["setuptoolstarbug==1.0"],
    dependency_links=["https://github.com/frishberg/setuptoolstarbug/archive/master.zip#egg=setuptoolstarbug-1.0"]
)
