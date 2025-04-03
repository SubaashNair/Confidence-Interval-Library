import os
from setuptools import setup, find_packages

# Ensure the current directory is correctly set
current_directory = os.path.abspath(os.path.dirname(__file__))

def read_file(filename):
    with open(os.path.join(current_directory, filename), encoding='utf-8') as f:
        long_description = f.read()
    return long_description

setup(
    name='confidence_interval',
    version='0.2.2',
    author='Subashanan Nair',
    author_email='subashanan.nair@gmail.com',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    url='https://github.com/SubaashNair/Confidence-Interval-Library',
    license='MIT',
    description='A comprehensive library for calculating and visualizing statistical confidence intervals.',
    long_description=read_file('README.md'),
    long_description_content_type='text/markdown',
    install_requires=[
        "numpy>=1.20.0",
        "scipy>=1.7.0",
        "matplotlib>=3.4.0",
    ],
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Statistics',
    ],
    keywords='statistics, confidence intervals, data analysis, visualization',
)

