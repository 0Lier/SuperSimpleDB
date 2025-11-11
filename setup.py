from setuptools import setup, find_packages

setup(
    name="ssdb",
    version="0.1.0",
    author="0Lier",
    description="A super simple, lightweight, and beginner-friendly database for bots, tools, and small apps that need quick file-based storage.",
    long_description=open("README.md", "r", encoding="utf-8").read(), 
    long_description_content_type="text/markdown",  
    packages=find_packages(),
    python_requires=">=3.8",
    license="GPL-3.0-or-later",  
    url="https://github.com/0Lier",  
)
