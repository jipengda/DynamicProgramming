from __future__ import absolute_import
from __future__ import print_function
import os
import subprocess

def listContrubutors(filename):


def extractBodyLines(lines):

class PythonHeader:
    def fix(self, filename, lines):

class StandaardHeader:
    def fix(self, filename, lines):

def findHeadersAndFiles():

def main():
    for header, filename in findHeadersAndFiles():
        print("Analyzing", filename)
        with open(filename) as f:
            lines = list(line.rstrip() for line in f)
        newLines = header.fix(filename, lines)
        if newLines != lines:
            print("=> actually modifying", filename)
            with open(filename, "w") as f:
                for line in newLines:
                    f.write(line + "\n")
                    
if __name__ == "__main__":
    main
