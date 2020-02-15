from setuptools import find_packages
from setuptools import setup


def parse_requirements(f):
    with open(f, 'r') as fp:
        for line in fp.readlines():
            yield line.strip()


def main():
    setup(
        name='cv2ools',
        use_scm_version=True,
        setup_requires=['setuptools_scm'],
        author='なるみ',
        author_email='weaper@gamil.com',
        packages=find_packages(),
        install_requires=list(parse_requirements('requirements.txt')),
    )


if __name__ == "__main__":
    main()
