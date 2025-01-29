#!/usr/bin/env python3.12

import argparse

parser = argparse.ArgumentParser(description="Python based command to read a content of file") #parser is a variable we can use anythin , argparse is a function
parser.add_argument('filename', help= 'name or path of the file to read the contents')
#args= parser.parse_args() #args is a variable
parser.add_argument('--line', type=int, help= 'number of line to read')

args=parser.parse_args()
print(args.filename)

try:
     with open(args.filename, "r") as fh:
        content= fh.readlines()
        limit=args.line

        if limit:
            content=content[0:limit]
        for line in content:
            print(line.strip())
        #print(fh.read())
except FileNotFoundError:
    print(f"The file {args.filename} not exists")
