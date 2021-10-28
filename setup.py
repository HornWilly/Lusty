import os
from setuptools import find_packages, setup, Extension

PACKAGE_DIR = os.path.join("resources", "libs")

setup(
    name="Lusty",
    description="Scrap general new from stove - epic seven",
    author="MAACHE Mehdi",
    author_email="mehdi.maache@gmail.com",
    version="0.0.1",
    url="https://github.com/hornwilly/Lusty",
    classifiers=[
        "Environment :: Console",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.8",
    ],
    keywords="epic7 stove automation scrapping",
    project_urls={
        "Bug Tracker": "https://github.com/hornwilly/Lusty",
        "Documentation": "https://github.com/hornwilly/Lusty",
        "Source Code": "https://github.com/hornwilly/Lusty",
    }
)
