import os

from setuptools import setup, find_packages


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['numpy', 
                'python-lzf @ https://github.com/rubenvanparys/pypcd/releases/download/0.1.2/python_lzf-0.2.4-cp36-cp36m-linux_x86_64.whl']

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

setup(
    author="Daniel Maturana",
    author_email='dimatura@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        "Intended Audience :: Science/Research",
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Multimedia :: Graphics :: 3D Modeling',
        'Topic :: Multimedia :: Graphics :: Capture',
        'Topic :: Multimedia :: Graphics :: Graphics Conversion',
    ],
    description="Read and write PCL .pcd files in python.",
    install_requires=requirements,
    license="BSD license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='pypcd',
    name='pypcd',
    packages=find_packages(include=['pypcd']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/dimatura/pypcd',
    version='0.1.1',
    zip_safe=False,
    data_files=[('config', ['HISTORY.rst'])]
)
