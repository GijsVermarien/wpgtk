"""wpgtk - setup.py"""
import setuptools
import os
import shutil

try:
    import wpgtk
except (ImportError, SyntaxError):
    print("error: wpgtk requires Python 3.5 or greater.")
    quit(1)


LONG_DESC = open('README.md').read()


VERSION = "4.5.1"
DOWNLOAD = "https://github.com/dylanaraps/pywal/archive/%s.tar.gz" % VERSION
WALL_DIR = os.path.expanduser('~') + '/.wallpapers'


setuptools.setup(
    name="wpgtk",
    packages=setuptools.find_packages(),
    version=VERSION,
    author="Fernando Vásquez",
    author_email="fmorataya.04@gmail.com",
    description="GTK+ theme/wallpaper manager which uses pywal as it's core",
    long_description=LONG_DESC,
    license="GPL2",
    url="https://github.com/deviantfero/wpgtk",
    download_url="https://github.com/deviantfero/wpgtk/archive/4.5.1.tar.gz",
    classifiers=[
        "Environment :: X11 Applications",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.5",
    ],
    entry_points={
        "console_scripts": ["wpg=wpgtk.__main__:main"]
    },
    python_requires=">=3.5",
    install_requires=[
        'Pillow>=4.2.1',
        'pywal>=0.6.0',
    ],
    include_package_data=True,
    data_files=[('/etc/wpgtk', ['wpgtk/misc/wpg.conf']),
                ('/usr/local/bin/', ['wpgtk/misc/wpg-install.sh'])]
)