'''
Translate image to ascii format
'''
import argparse
import logging
import os
import sys
import numpy as np
from PIL import Image, ImageFilter, ImageOps


def parse(arguments):
    '''Parse arguments'''
    parser = argparse.ArgumentParser(description='Transform jpeg image to ASCII')
    parser.add_argument('--dir', '-d', type=str,
                        help='Path to directory with files')
    parser.add_argument('--inverse', '-i', action='store_true',
                        help='Invert image')
    parser.add_argument('--mod', '-m', action='store_true',
                        help='''Filter image to find edges before transformation,
                                sharpen by default''')
    parser.add_argument('--output', '-o', type=str, help='Output file')
    parser.add_argument('--path', '-p', type=str, help='Path to file')
    parser.add_argument('--resize', '-r', type=int, nargs=2,
                        help='Resize image to x_s, y_s')
    parser.add_argument('--verbose', '-v', action='store_true')
    args = parser.parse_args(arguments)
    return args


def prepare_image(path, arguments):
    '''Transform image from path to monochrome, filter, resize and invert
       if there is a need, as seen in arguments'''
    img = Image.open(path)
    img = img.convert('L')
    mod = arguments.mod
    if arguments.resize:
        x_size, y_size = arguments.resize
        img = img.resize((x_size, y_size))
    if mod:
        img = img.filter(ImageFilter.FIND_EDGES)
    else:
        img = img.filter(ImageFilter.SHARPEN)
    if arguments.inverse:
        img = ImageOps.invert(img)
    return img


def create_ascii(img, ascii_arr):
    '''Create ASCII art from img'''
    x_size, y_size = img.size
    img_arr = np.array(img)
    result = ''
    logging.info('Begin loop')
    logging.info('Size %d x %d, %d pixels', y_size, x_size, x_size*y_size)
    for y in range(y_size):
        for x in range(x_size):
            brightness = img_arr[y, x]  # [row, column]
            result = result+ascii_arr[brightness]
        if x == x_size-1:
            logging.info('%d/%d', y, y_size)
            result = result + '\n'
    return result


def main(arguments):
    '''Main function, translates all jpg files from directory to ASCII'''
    translate = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
    long_ascii = [i*4 for i in translate]
    long_ascii = ''.join(long_ascii)
    if arguments.dir:
        os.chdir(arguments.dir)
        files_list = os.listdir()
        path_list = list(filter(lambda x: 'jpg' in x, files_list))
        logging.info(path_list)
        for path in path_list:
            if arguments.inverse:
                new_path = path[:-4]+'_inverse.txt'
            else:
                new_path = path[:-4]+'.txt'
            logging.info('Beginning of creating ascii from %s, writing to %s',
                         path, new_path)
            img = prepare_image(path, arguments)
            res = create_ascii(img, long_ascii)
            with open(new_path, 'w', encoding='utf-8') as f:
                f.write(res)
            logging.info('End of creating ascii, written to %s', new_path)
    if arguments.path:
        path = arguments.path
        if arguments.output:
            new_path = arguments.output
        else:
            if arguments.inverse:
                new_path = path[:-4]+'_inverse.txt'
            else:
                new_path = path[:-4]+'.txt'
        logging.info('Beginning of creating ascii from %s, writing to %s', path,
                     new_path)
        img = prepare_image(path, arguments)
        res = create_ascii(img, long_ascii)
        with open(new_path, 'w', encoding='utf-8') as f:
            f.write(res)
        logging.info('End of creating ascii, written to %s', new_path)


if __name__ == "__main__":
    args = parse(sys.argv[1:])
    if args.verbose:
        logging.basicConfig(level='INFO')
    else:
        logging.basicConfig(level='WARNING')
    main(args)
