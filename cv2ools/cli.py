from pathlib import Path

import click
import cv2

from .core import VideoWriter


@click.group()
def cli():
    pass


@cli.command()
@click.argument('image-dir')
@click.option('-o', '--output', default=None)
@click.option('--fps', default=60)
def merge(image_dir, output, fps):
    r"""Create video from images"""
    image_extensions = ['.jpg', '.jpeg', '.png']

    image_dir = Path(image_dir)

    if output is None:
        output = image_dir.with_suffix('.mp4')

    paths = [path for path in sorted(image_dir.iterdir()) if path.suffix in image_extensions]

    with VideoWriter(output, fps) as writer:
        for path in paths:
            image = cv2.imread(str(path))
            writer.write(image)


if __name__ == '__main__':
    cli()
