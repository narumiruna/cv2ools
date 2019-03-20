import argparse
import os
from glob import glob
from logging import getLogger

import cv2
from tqdm import tqdm

LOGGER = getLogger(__name__)


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--root', type=str)
    parser.add_argument('-o', '--output', type=str, default='output.mp4')
    parser.add_argument('--fps', type=int, default=30)
    return parser.parse_args()


def main():
    args = parse()

    paths = sorted(glob(os.path.join(args.root, '*.jpg')))

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter(args.output, cv2.CAP_FFMPEG, fourcc,
                                   args.fps, (1280, 720))

    for path in tqdm(paths):
        img = cv2.imread(path)
        if img is not None:
            img = img[:720, :, :]
            video_writer.write(img)
        else:
            LOGGER.info('Cannot read image file: %s', path)

    video_writer.release()


if __name__ == "__main__":
    main()
