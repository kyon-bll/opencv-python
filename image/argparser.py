import argparse

parser = argparse.ArgumentParser(description='Edit img and Output image in `output` dir.')

subparsers = parser.add_subparsers(dest='subcommand')

def add_subparser(subcommand, **kwargs):
    subparser = subparsers.add_parser(subcommand, **kwargs)
    subparser.add_argument('input_img', help='input image path')

    return subparser


parser_rotate = add_subparser('rotate', help='rotate img by degree')
parser_rotate.add_argument('degree', type=float, help='can accept float')

parser_zoom = add_subparser('zoom', help='zoom img')
parser_zoom.add_argument('scale', type=float, help='scale int times')
