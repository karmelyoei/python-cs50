from setuptools import setup

setup(
    author="CS50",
    author_email="sysadmins@cs50.harvard.edu",
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    description="CS50 library for Python",
    install_requires=["SQLAlchemy"],
    keywords="cs50",
    name="cs50",
    packages=["cs50"],
    url="https://github.com/cs50/python-cs50",
    version="1.3.0"
)