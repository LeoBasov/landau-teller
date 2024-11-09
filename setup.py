from setuptools import setup 

setup( 
	name='landau_teller', 
	version='0.1.1', 
	description='Evaluates 0D Ladau-Teller like relaxation of internal degrees of freedom for mixtures with polyatomic species', 
	author='Leo Basov', 
	packages=['landau_teller'], 
	install_requires=[ 
		'numpy',
	], 
) 
