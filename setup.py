import subprocess

from setuptools import find_packages
from setuptools import setup


def get_version():
    tag = subprocess.check_output(['git', 'describe', '--tags']).decode('utf-8')
    version = tag.lstrip('v').split('-')[0]
    return version


def parse_requirements(f):
    lines = []
    with open(f, 'r') as fp:
        for line in fp.readlines():
            lines.append(line.strip())
    return lines


def main():
    requirements = parse_requirements('requirements.txt')

    setup(
        name='cv2ools',
        version=get_version(),
        author='なるみ',
        author_email='weaper@gamil.com',
        packages=find_packages(),
        install_requires=requirements,
    )


if __name__ == "__main__":
    main()
