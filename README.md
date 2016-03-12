# pysh 1

Run shell commands in a pythonic way.

## Install

Install using setup script:

	#  python setup.py install

## Use

Import commands and call them:

	>>> from pysh import echo
	>>> str(echo("abc"))
	'abc\n'

Use pipelines:

	>>> from pysh import echo, bc
	>>> str(echo("2 + 1") | bc())
	'3\n'
