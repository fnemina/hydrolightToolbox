from setuptools import setup, find_packages

setup(
    name='hydrolightToolbox',
    version='0.1.0',
    description='A toolbox for working with hydrolight data',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'matplotlib',
        'xarray'
    ],
    extras_require={
        'pint': ['pint']
    },
    python_requires='>=3.6',
    author='Francisco Nemiña',
    author_email='fnemina@conae.gov.ar',
    url='https://github.com/fnemina/hydrolightToolbox',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Scientific/Engineering :: Atmospheric Science'
    ],
    keywords='oceanography, hydrolight, remote sensing'
)
