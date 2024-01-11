import sys
import os
sys.path.append('/usr/lib/freecad-python3/lib/')
from pathlib import Path
from FreeCAD import Part
from Part import Shape
#import glob
#use glob.glob for a list of files
def conversion(input_path, output_path):
    # Check if the input file exists
    if not os.path.isfile(input_path):
        print(f"Input file not found: {input_path}")
        return

    try:
    	name = os.path.basename(input_path).split('.')[0]
    	output_path = output_path + name + '.stl'
        # Read the STEP file
        body = Shape()
        body.read(input_path)

        # Export the STL file
        tesselation_param = 0.1
        body.exportStl(output_path, tesselation_param)
        print(f'STL file exported successfully at path: {output_path}')

    except Exception as e:
        print(f'Error processing {input_path}: {e}')

# Example usage
if __name__ == "__main__":
    # Ask the user for input and output paths
    input_path = input("Enter the path to the input .stp file: ")
    output_path = input("Enter the path for the output .stl file: ")
	
    # Call the conversion function
    conversion(input_path, output_path)
