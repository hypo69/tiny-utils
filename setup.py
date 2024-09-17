from setuptools import setup, find_packages

setup(
    name='tiny_utils',  # Package name
    version='0.1.0',  # Package version
    packages=find_packages(),  # Automatically find all packages
    install_requires=[  # Dependencies
        #'requests>=2.25.1',
        # other dependencies
    ],
    description='Lightweight utilities for everyday tasks',  # Description
    long_description=open('README.md').read(),  # Long description from file
    long_description_content_type='text/markdown',
    url='https://github.com/hypo69/tiny-utils',  # Project URL
    author='hypo69',
    author_email='one.last.bit@gmail.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.12',  # Minimum Python version
)
