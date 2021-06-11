# Python SVG to G-Code Converter
A fast svg to gcode converter, forked from [andriesbron/svg2gcode](https://github.com/andriesbron/svg2gcode).

This fork offers a more flexible CLI and the hability to generate other gcode flavors such as FDM 3D Printing.

BEWARE: This is still an experimental tool and you should be very careful when using the generated g-codes. Make sure to check them on a visualizer before running.

## Fork Features
- Python 3.3+ support
- Command Line Interface
- Machine Classes: Router, 3D Printer
- Default + Custom config file
- Custom Output
- Package encapsulation

## Installation
Clone this repository.
```
git clone https://github.com/hugoaboud/py-svg2gcode.git
```

## Usage
### Python Package
Place the `svg2code/` folder into your project root, then you can simply import and run it:
```python
from svg2gcode import generate_gcode
gcode = generate_gcode('test0.svg')
print(gcode)
```

### Standalone (CLI)

```
python -m svg2gcode [-h] [-o GCODE] [-d] [-c CONFIG] [--3d] SVG

positional arguments:
  SVG          input .svg file

optional arguments:
  -h, --help   show this help message and exit
  -o GCODE     output .gcode file (default: gcode/*.svg)
  -d, --debug  output debug info and save log
  -c CONFIG    config file (overrides default.config)
  --3d         generate G-Code for 3D printing instead of mill/laser
```

Convert `input.svg` into `gcode/input.gcode`:
```
python -m svg2gcode input.svg
```

3D Printing FDM mode
```
python -m svg2gcode input.svg --3d
```

Custom config file. The values not present on the custom file are loaded from `default.config`.
Make sure to override all the relevant values for your machine.
```
python -m svg2gcode input.svg -c custom.config
```

Custom output file.
```
python -m svg2gcode input.svg -o custom.gcode
```

## Details
The compiler is based on the eggbot project and it basically converts all of the SVG shapes into bezier curves. The bezier curves are then recursively sub divided until desired smoothness is achieved. The sub curves are then approximated as lines which are then converted into g-code.
