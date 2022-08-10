from black_junit import __version__
from setuptools import setup

setup(
    name="black-junit",
    version=__version__,
    description="Tool for generation JUnit report from black/blue output",
    url="https://github.com/quantum-0/black-junit",
    author="Anton Kurenkov (Quantum0)",
    author_email="quantum0@mail.ru",
    license="MIT",
    keywords="automation ci black blue gitlab",
    packages=["black_junit"],
    install_requires=["junit_xml==1.9"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Quality Assurance",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    entry_points={
        "console_scripts": [
            "black-junit=black_junit:main",
        ]
    },
)
