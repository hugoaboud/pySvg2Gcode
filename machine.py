import math
class Router:

    '''G-code emitted at the start of processing the SVG file'''
    @staticmethod
    def preamble(config):
        return "G28\nG1 Z0.0\nM05\n"

    '''G-code emitted at the end of processing the SVG file'''
    @staticmethod
    def postamble(config):
        return "G28\n"

    '''G-code emitted before processing a SVG shape'''
    @staticmethod
    def shape_preamble(config):
        return "G4 P0.2\n"

    '''G-code emitted after processing a SVG shape'''
    @staticmethod
    def shape_postamble(config):
        return "G4 P0.2\nM05\n"

    '''G-code for a travel (non-printing) move'''
    @staticmethod
    def travel(config, org_x, org_y, x, y):
        return "G0 X%0.2f Y%0.2f\nM03\n" % (x, y)

    '''G-code for a print move'''
    @staticmethod
    def print(config, org_x, org_y, x, y):
        return ("G0 X%0.1f Y%0.1f\n" % (x, y))

class Printer3D:

    @staticmethod
    def preamble(config):
        # home
        str = "G28\n"
        # heat bed
        str += "M190 S"+config['3DPRINT MATERIAL']['bed_temperature']+"\n"
        # extruder
        str += "M109 S"+config['3DPRINT MATERIAL']['e0_temperature']+"\n"
        # fan
        str += "M106 S"+config['3DPRINT MATERIAL']['fan']+"\n"
        # z clearance (5mm)
        str += "G0 Z"+config['MACHINE']['z_clearance']+"\n"
        # feed rate
        str += "G1 F"+config['MACHINE']['feed_rate']+"\n"
        return str

    @staticmethod
    def postamble(config):
        # home
        return "G28\n"

    @staticmethod
    def shape_preamble(config):
        return ""

    @staticmethod
    def shape_postamble(config):
        return ""

    @staticmethod
    def travel(config, org_x, org_y, x, y):
        # z clearance (5mm)
        str = "G0 Z"+config['MACHINE']['z_clearance']+"\n"
        # travel move
        str += "G0 X%0.2f Y%0.2f\n" % (x, y)
        # z layer height
        str += "G0 Z"+config['3DPRINT MACHINE']['layer_height']+"\n"
        return str

    @staticmethod
    def print(config, org_x, org_y, x, y):
        nozzle = float(config['3DPRINT MACHINE']['nozzle_diameter'])
        layer = float(config['3DPRINT MACHINE']['layer_height'])
        flow = float(config['3DPRINT MACHINE']['flow_multiplier'])
        filament = float(config['3DPRINT MATERIAL']['filament_diameter'])/2
        length = math.sqrt((x-org_x)*(x-org_x)+(y-org_y)*(y-org_y))

        volume = nozzle * layer * length * flow;
        extrude = volume/(3.14159265359*filament*filament)

        return "G1 X%0.2f Y%0.2f E%0.2f\n" % (x, y, extrude)
