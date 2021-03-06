"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import find_packages, setup, Command
# To use a consistent encoding
from codecs import open
from os import path
from shutil import rmtree
import os
import sys

here = path.abspath(path.dirname(__file__))

VERSION = None

about = {}
if not VERSION:
    with open(os.path.join(here, '__version__.py')) as f:
        exec(f.read(), about)
else:
    about['__version__'] = VERSION


class UploadCommand(Command):
    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(os.path.join(here, 'dist'))
        except OSError:
            pass

        self.status('Building Source and Wheel (universal) distribution…')
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))

        self.status('Uploading the package to PyPI via Twine…')
        os.system('twine upload dist/*')

        self.status('Pushing git tags…')
        os.system('git tag v{0}'.format(about['__version__']))
        os.system('git push --tags')

        sys.exit()


setup(
    name='scrapy_script',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version=about['__version__'],

    description='Run a Scrapy spider programmatically from a script or a Celery task - no project required.',
    long_description='scrapy-script allows you to invoke one or more spiders from a script, have them all run in '
                     'parallel, and get the results back as a single list. No scrapy project, no boilerplate, '
                     'no hassle. Modified from https://github.com/jschnurr/scrapyscript',

    # The project's main homepage.
    url='https://github.com/xkl1bur/scrapy-script',

    # Author details
    author='xkl1bur',
    author_email='xksdev@gmail.com',

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.8',
        'Framework :: Scrapy',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License'
    ],

    # What does your project relate to?
    keywords='scrapy',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=[],

    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    py_modules=['scrapy_script'],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=['Scrapy>=1.4.0',
                      'billiard>=3.5.0.2',
                      ],

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    package_data={
    },

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    # data_files=[('my_data', ['data/data_file'])],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
    },

    # $ setup.py publish support.
    cmdclass={
        'upload': UploadCommand,
    },
)
