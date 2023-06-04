from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in ruphasoft_rupha/__init__.py
from ruphasoft_rupha import __version__ as version

setup(
	name="ruphasoft_rupha",
	version=version,
	description="Frappe app for RUPHA (Rural Private Hospitals Association)",
	author="mohamud@rupha.co.ke",
	author_email="mohamud.a.a@rupha.co.ke",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
