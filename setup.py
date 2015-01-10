from setuptools import setup, find_packages
import sys, os

version = '0.0.1'

setup(name='playwork',
      version=version,
      description="tornado, web framework, framework",
      long_description="""\
a web framework based on the Tornado project""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='playwork, tornado, web, webframework, framework',
      author='younger shen',
      author_email='younger.x.shen@gmail.com',
      url='http://github.com/youngershen',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
