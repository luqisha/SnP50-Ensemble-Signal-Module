from setuptools import setup, find_packages

setup(
    name='ensemble_strategy',
    version='0.1',
    description='An ensemble strategy using 50 diversified stocks in the S&P 500 index',
    author='luqisha',
    packages=find_packages(),
    install_requires=[
        'hurst',
    ],
)
