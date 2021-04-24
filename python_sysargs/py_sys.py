import argparse

ap = argparse.ArgumentParser()

# Add the arguments to the parser
ap.add_argument("-abc", "--foperand", required=True,
   help="first operand")
ap.add_argument("-bcd", "--soperand", required=True,
   help="second operand")
args = vars(ap.parse_args())

print(f"First operand  :: {args['foperand']}")
print(f"Second operand :: {args['soperand']}")

#----------------------------------------------------------
# Command to run : python py_sys.py -abc <value>       -bcd <value>
# Command to run : python py_sys.py --foperand <value> --soperand <value>