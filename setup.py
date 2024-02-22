from setuptools import setup, find_packages

setup(
    name='IndianNameExtractor',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',  # Add all the dependencies your package needs here
        'scikit-learn',
        # etc.
    ],
)