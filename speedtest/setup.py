from setuptools import setup

APP = ['Speedtest.py']
OPTIONS = {
  'iconfile':'speedtest.icns',
  'argv_emulation':True,
  'packages':['certifi'],
  }

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)