from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
	name='Smudge',
	version='1.0.0',
	py_modules=['smudge'],
	install_requires=[
		'Click',

	],
	entry_points='''
		[console_scripts]
		smudge=smudge:cli
	''',

	author="Tom Hill",
	author_email="tom@hill.xyz",
	description="Smudge: For better blotting from the command line!",
	long_description=long_description,
    long_description_content_type="text/markdown",
)
