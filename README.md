# Python SVG to G-Code Converter
A fast svg to gcode compiler forked from [vishpat/svg2gcode](https://github.com/vishpat/svg2gcode).

This library takes an svg file `location/my_file.svg` and outputs the gcode conversion to a folder in the same directory `location/gcode_output/my_file.gcode`.

The file `config.py` contains the configurations for the conversion (printer bed size etc).

## Fork information
The original has an error with svg files from inkscape, that is solved in this fork.

From inkscape: export to plain svg, then convert the file using this python module. 
Make sure that you have converted all objects to paths :-)

I don't know how it works, but it seems to work.

You might take a look at https://www.youtube.com/watch?v=Dwqlf5iirbM for using it for laser cutting


## Installation
Simply clone this repo.
```
git clone https://github.com/pjpscriv/py-svg2gcode.git
```

## Usage
### As a Python module
To import it into your existing python project:
```python
import py-svg2gcode
```
or
```python
import generate_gcode from py-scvg2gcode
```
### As a Python Command
```
python svg2gcode.py
```

## Details
The compiler is based on the eggbot project and it basically converts all of the SVG shapes into bezier curves. The bezier curves are then recursively sub divided until desired smoothness is achieved. The sub curves are then approximated as lines which are then converted into g-code.
