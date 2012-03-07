from setuptools import setup, find_packages

import avi2mkv

setup(
    name=avi2mkv.__uname__,
    version=avi2mkv.__version__,
    description="Simple AVI to MKV converter",
    long_description='\n'.join([open('README.rst').read()]),

    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Multimedia :: Sound/Audio :: Conversion",
    ],
    keywords='conversor,avi,mkv,simple',

    author=avi2mkv.__author__,
    author_email=avi2mkv.__email__,
    url=avi2mkv.__url__,
    license=avi2mkv.__license__,

    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
    scripts = ['avi2mkv'],
)

# vim: ai ts=4 sts=4 et sw=4
