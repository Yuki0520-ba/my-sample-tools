
import pathlib

from setuptools import setup, find_packages

here = pathlib.Path(__file__).parent.resolve()
install_requires = (here / 'requirements.txt').read_text(encoding='utf-8').splitlines()

setup(
    install_requires = install_requires,
    name = "sample-cli",
    version = "0.0.1",
    package_dir={"": "src"},
    packages= find_packages("src"),
    entry_points={
        'console_scripts': [
            'samplecli = sample_cli.cli:main',
        ],
    },  
)
