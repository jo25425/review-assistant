from os.path import isfile, dirname

version_file = f'{dirname(__file__)}'

if isfile(version_file):
    with open(version_file) as f:
        __version__ = f.read().strip()
