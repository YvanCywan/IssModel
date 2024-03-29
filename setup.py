from setuptools import setup, find_packages

setup(
    name='iss-model',
    version='0.0.1',
    packages=find_packages(where='src'),
    include_package_data=True,
    install_requires=[
        "numpy",
        "pytest",
        "pip",
        "setuptools",
        "scipy",
    ],
    author='Yvan Cywan',
    description='A non working model of the ISS',
    license='MIT'
)

