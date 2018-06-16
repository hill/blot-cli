from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
	name='Blot',
	version='1.0.0',
	py_modules=['blot'],
	install_requires=[
		'Click',

	],
	entry_points='''
		[console_scripts]
		blot=blot:cli
	''',

	author="Tom Hill",
	author_email="tom@hill.xyz",
	description="Blot-CLI: For better blotting from the command line!",
	long_description=long_description,
    long_description_content_type="text/markdown",
)
