from setuptools import setup, find_packages

setup(
    name='elasticnet',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scikit-learn',
        'pytest',
    ],
)
