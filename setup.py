#! /usr/bin/env python

import setuptools

from business_rules import __version__ as version

with open('HISTORY.rst') as f:
    history = f.read()

description = 'Python DSL for setting up business intelligence rules that can be configured without code'

setuptools.setup(
        name='business-rules',
        version=version,
        description=description,
        long_description=history,
        author='Venmo',
        author_email='open-source@venmo.com',
        url='https://github.com/venmo/business-rules',
        packages=['business_rules'],
        license='MIT'
)
