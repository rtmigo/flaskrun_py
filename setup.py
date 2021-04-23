from pathlib import Path

from setuptools import setup, find_packages

readme = (Path(__file__).parent / 'README.md').read_text()

setup(
  name="flask_bgprocess",
  version="1.0.0",

  author="Artёm IG",
  author_email="ortemeo@gmail.com",
  url='https://github.com/rtmigo/flask_bgprocess_py',

  packages=find_packages(),
  install_requires=['bgprocess @ git+ssh://git@github.com/rtmigo/bgprocess_py#egg=bgprocess', 'pip'],

  description="Runs Flask server locally in a background process, so in can be tested with HTTP requests",

  long_description=readme,
  long_description_content_type='text/markdown',

  license='MIT',

  keywords="""flask unit testing test  unit-test wsgi process timeout""".split(),

  # https://pypi.org/classifiers/
  classifiers=[
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    'License :: OSI Approved :: MIT License',
    'Topic :: Software Development :: Documentation',
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Operating System :: POSIX",
  ],

  test_suite='test_unit.suite',
  tests_require=['flask', 'requests'],
)
