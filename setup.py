#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from setuptools import setup, find_packages
from setuptools.command.install import install as InstallCommand
from setuptools.command.test import test as TestCommand

version = "0.12"
requirements = "libxml2-dev libxslt-dev python-dev"


class Install(InstallCommand):

    def run(self):

        #params = "{install_params} {requirements}".format(install_params="install", requirements=requirements)
        #cmd = "{command} {params}".format(command="apt-get", params=params)
        #proc = subprocess.Popen(cmd, shell=True)
        # proc.wait()
        InstallCommand.run(self)


class Test(TestCommand):

    user_options = [('pytest-args=', 'a', "")]

    def initialize_options(self):

        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):

        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):

        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)

setup(
    name='webdavclient3',
    version=version,
    packages=find_packages(),
    requires=['python (>= 2.7.6)'],
    install_requires=['requests', 'lxml', 'argcomplete'],
    scripts=['wdc'],
    test_suite='tests',
    tests_require=['pytest'],
    cmdclass={'install': Install, 'test': Test},
    description='WebDAV client, based on original package https://github.com/designerror/webdav-client-python but '
                'uses requests instead of PyCURL',
    long_description=open('README.rst').read(),
    author='Evgeny Ezhov',
    author_email='ezhov.evgeny@gmail.com',
    url='https://github.com/ezhov-evgeny/webdav-client-python-3',
    license='MIT License',
    keywords='webdav, client, python, module, library, packet, Yandex.Disk, Dropbox, Google Disk, Box, 4shared',
    classifiers=[
        'Environment :: Console',
        'Environment :: Web Environment',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Operating System :: Microsoft',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
