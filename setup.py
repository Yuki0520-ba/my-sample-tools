
import pathlib

from setuptools import setup, find_packages

here = pathlib.Path(__file__).parent.resolve()
install_requires = (here / 'requirements.txt').read_text(encoding='utf-8').splitlines()

setup(
    install_requires = install_requires,
    package_dir=("", "src"),
    packages= find_packages("src"),
    entry_points={
        "console_scripts": [
            "sample-cli = sample-cli.cli:main"
        ]
    }  
)
