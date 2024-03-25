from setuptools import find_packages
from setuptools import setup

with open("requirements.txt") as f:
    content = f.readlines()
requirements = [x.strip() for x in content if "git+" not in x]

setup(name='reviewassistant',
      version="0.0.1",
      description="Review Assistant",
      license="MIT",
      author="Le Wagon #1601 Team 6",
      url="https://github.com/jo25425/review-assistant/",
      install_requires=requirements,
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False)
