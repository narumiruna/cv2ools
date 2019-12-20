import argparse
import os
from glob import glob

import cv2
from tqdm import tqdm

import cv2ools


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--root', type=str)
    parser.add_argument('-o', '--output', type=str, default='output.mp4')
    parser.add_argument('--fps', type=int, default=30)
    return parser.parse_args()


def read_images(paths):
    for path in tqdm(paths):
        img = cv2.imread(path)
        if img is not None:
            yield img
        else:
            break


def main():
    args = parse_args()
    paths = sorted(glob(os.path.join(args.root, '*.jpg')))
    cv2ools.write_video(read_images(paths), args.output)


if __name__ == "__main__":
    main()
