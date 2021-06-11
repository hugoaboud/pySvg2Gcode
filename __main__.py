import argparse
import os
from svg2gcode.main import generate_gcode

# Command Line Interface

parser = argparse.ArgumentParser(description='Converts SVG files to G-Code.')
parser.add_argument('file', metavar='SVG', type=str, nargs=1,
                    help='input .svg file')
parser.add_argument('-o', metavar='GCODE', dest='out', nargs=1,
                    help='output .gcode file (default: gcode/*.svg)')
parser.add_argument('-d', '--debug', dest='debug', action='store_true',
                    help='output debug info and save log')
parser.add_argument('-c', metavar='CONFIG', dest='config', type=str, nargs=1,
                    help='config file (overrides default.config)')
parser.add_argument('--3d', dest='print3d', action='store_true',
                    help='generate G-Code for 3D printing instead of mill/laser')

args = parser.parse_args()

# Default outfile
outdir = os.path.dirname(os.path.realpath(args.file[0]))
outfile = ''
if (args.out):
    outfile = os.path.join(outdir, args.out[0])
else:
    outdir = os.path.join(outdir,"gcode")
    outfile = os.path.join(outdir, args.file[0].split(".svg")[0] + '.gcode')
if (args.debug):
    print("Output File: "+outfile)

# Make Output Directory
if not os.path.exists(outdir):
    os.makedirs(outdir)


# Run script
gcode = generate_gcode(args.file[0], cfg=args.config, print3d=args.print3d, debug=args.debug)

# Write to file
ofile = open(outfile, 'w+')
ofile.write(gcode)
ofile.close()
