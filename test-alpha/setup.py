import glob
from setuptools import setup, find_packages
import os
import codecs

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
ALPHA_LIB_DIR = 'test_alpha'
ALPHA_LIB_PATH = CURRENT_DIR + '/' + ALPHA_LIB_DIR


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


def get_version_from_init():
    return get_version(f"{ALPHA_LIB_DIR}/__init__.py")


print(CURRENT_DIR, ALPHA_LIB_PATH)

exclude_py_packages = ['__init__', 'setup']
py_packages = [f.split('/')[-1][:-3] for f in
               glob.glob('{}/*.py'.format(ALPHA_LIB_PATH))]
py_packages = [p for p in py_packages if p not in exclude_py_packages]
print(py_packages)

setup(
    name='{}'.format(ALPHA_LIB_DIR),
    version=get_version_from_init(),
    packages=find_packages(exclude=['{}.examples'.format(ALPHA_LIB_DIR)]),
   # install_requires=['contek-op-lib @ git+ssh://git@github.com/contek-io/contek-op-lib.git@v1.3.3+prod'],
)
