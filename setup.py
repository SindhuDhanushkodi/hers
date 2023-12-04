from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in hers/__init__.py
from hers import __version__ as version

setup(
	name="hers",
	version=version,
	description="I want",
	author="Sindhu",
	author_email="sindhu@yuvabe.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
