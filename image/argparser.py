import argparse

parser = argparse.ArgumentParser(description='Edit img and Output image in `output` dir.')

subparsers = parser.add_subparsers(dest='subcommand')

parser_rotate = subparsers.add_parser('rotate', help='rotate img by degree')
parser_rotate.add_argument('input_img',  help='input image path')
parser_rotate.add_argument('degree', type=float, help='can accept float')

parser_zoom = subparsers.add_parser('zoom', help='zoom img')
parser_zoom.add_argument('scale', type=float, help='scale int times')
