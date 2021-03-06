
from setuptools import setup, find_packages

setup(
    name = "Boids",
    version = "0.1.0",
    packages = find_packages(exclude=['*test']),
	scripts = ['scripts/boids'],
	include_package_data=True,
	package_data = {'boids': ['config.yaml']},
    install_requires = ['matplotlib', 'setuptools'] # for some reason, the installer didn't like me adding 'yaml' and 'random' in this list
)