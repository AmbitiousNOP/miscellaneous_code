#!/usr/bin/env python

from setuptools import setup


setup(name='temperature',
      version='2.0',
      description='Temperature management',
      url='https://umbctraining.com',    # Should  be the homepage of project
      author='UMBC Training Centers',
      author_email='instructors@umbctraining.com',
      packages=['temperature', 'temperature.foods', 'temperature.scales'])
