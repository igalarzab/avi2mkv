from setuptools import setup, find_packages

__uname__ = 'avi2mkv'
__long_name__ = 'Simple AVI to MKV converter'
__version__ = '1.1'
__author__ = 'Jose Ignacio Galarza'
__email__ = 'igalarzab@gmail.com'
__url__ = 'http://github.com/igalarzab/avi2mkv'
__license__ = 'MIT'

setup(
    name=__uname__,
    version=__version__,
    packages=find_packages(),

    author=__author__,
    author_email=__email__,
    description="Simple AVI to MKV converter",
    long_description='\n'.join([open('README.md').read()]),
    license=__license__,
    url=__url__,
    keywords='conversor,avi,mkv,simple',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        "Environment :: Console",
        'License :: OSI Approved :: MIT License',
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Multimedia :: Sound/Audio :: Conversion",
    ],

    py_modules=['avi2mkv'],
    include_package_data=True,
    install_requires=[],
    entry_points={
        'console_scripts': ['avi2mkv = avi2mkv:main']
    },
)

# vim: ai ts=4 sts=4 et sw=4
