from setuptools import find_packages, setup


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
        version='0.0.1',
        author='なるみ',
        author_email='weaper@gamil.com',
        packages=find_packages(),
        install_requires=requirements,
    )


if __name__ == "__main__":
    main()
