from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="travelperk-python-api-types",
    version="1.0.5",
    description="Python types for the travelperk API entities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/namelivia/travelperk-python-api-types",
    author="José Ignacio Amelivia Santiago",
    author_email="jignacio.amelivia@gmail.com",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    keywords="travelperk, api",
    install_requires=["pydantic"],
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    python_requires=">=3.8, <4",
    project_urls={
        "Bug Reports": "https://github.com/namelivia/travelperk-python-api-types/issues",
    },
)
