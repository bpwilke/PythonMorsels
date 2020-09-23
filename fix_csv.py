'''This week we're going to normalize CSV files by writing a program, fix_csv.py, that turns a pipe-delimited file into a comma-delimited file. I'll explain how it should work by example.

Your original file will look like this:

Reading|Make|Model|Type|Value
Reading 0|Toyota|Previa|distance|19.83942
Reading 1|Dodge|Intrepid|distance|31.28257
You'll then run your script by typing this at the command line:

$ python fix_csv.py cars-original.csv cars.csv
Note : "$" is not typed; that is simply the beginning of the prompt.

Your fixed file should then look like this:

Reading,Make,Model,Type,Value
Reading 0,Toyota,Previa,distance,19.83942
Reading 1,Dodge,Intrepid,distance,31.28257
Note that it's valid for a comma to be in your input data, but you'll need to surround data cells with commas in them by double quotes when writing your output file.

It's also valid for a quote character to be in your input (you'll need to double up quotes because that's how CSV escaping works.

See the hints if you need help working with CSV files in Python.

Bonus 1

For the first bonus, I want you to allow the input delimiter and quote character (" by default) to be optionally specified. ✔️

For example any of these should work (all specify input delimiter as pipe and the last two additionally specifies the quote character as single quote):

$ python fix_csv.py --in-delimiter="|" cars.csv cars-fixed.csv
$ python fix_csv.py cars.csv cars-fixed.csv --in-delimiter="|"
$ python fix_csv.py --in-delimiter="|" --in-quote="'" cars.csv cars-fixed.csv
$ python fix_csv.py --in-quote="|" --in-delimiter="," cars.csv cars-fixed.csv

This bonus will require looking into parsing command-line arguments with Python. There are some standard library modules that can help you out with this. There are 3 different solutions in the standard library actually, but only one I'd recommend.

Also note that if you're going to need Python to parse your CSV files for this bonus (or else you'll re-implement quite a bit of CSV-parsing code that's baked-in to Python).

Bonus 2

For the second bonus, try to automatically detect the delimiter if an in-delimiter value isn't supplied (don't assume it's pipe and quote, figure it out). ✔️

This second bonus is a bit trickier and I don't expect it to work correctly for all files. Don't be afraid to check the hints for this one.
'''

import csv
import argparse

my_parser = argparse.ArgumentParser()

# Add the arguments
my_parser.add_argument('InputFile', metavar='inputfile', type=str, help='The input file name')
my_parser.add_argument('OutputFile', metavar='outputfile', type=str, help='The output file name')
my_parser.add_argument('--in-delimiter', action='store', metavar='indelimiter', type=str, help='The delimiter')
my_parser.add_argument('--in-quote', action='store', metavar='inquote', type=str, help='The in-quote')

# Execute the parse_args() method
args = vars(my_parser.parse_args())

# Process our delimiter and inquote to accomodate the defaults requirements

in_delimiter = str()
in_quote = str()

if args['in_delimiter'] == None:
	in_delimiter = '|'
else:
	in_delimiter = args['in_delimiter']

if args['in_quote'] == None:
	in_quote = '"'
else:
	in_quote = args['in_quote']

# main part of the code that opens write file, then opens read file, parses

with open(args['OutputFile'], 'w') as outputfile:
    with open(args['InputFile'], 'r') as openfile:
        csvfile = csv.reader(openfile, delimiter = in_delimiter, quotechar = in_quote)
        outputwriter = csv.writer(outputfile, delimiter=',')
        for row in csvfile:
            outputwriter.writerow(row)


