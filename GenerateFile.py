import sys

'''
Command line arguments.
First argument is the name of the header file to generate. Will default to "generatedConstChars.h".
Second argument is the text file containing the files that will be used to generate the header.
'''

headerFileName = None
if(len(sys.argv) != 3):
    exit()
    #headerFileName = "generatedConstChars.h"


headerFileName = sys.argv[1] + ".h"
files = sys.argv[2]


header = open(headerFileName, "w")
header.write("#pragma once\n")

gens = open(files, "r").read().split("\n")

# Creates a string formatted as c++ constexpr const char* variableName = fileContents
def FileToConstChar(filePath : str, variableName : str):
    file = open(filePath, "r")
    contents = file.read()
    contents = "R\"(" + contents + ")\";"
    file.close()
    lastIndex = filePath.rfind("/")
    fileName = filePath[lastIndex + 1 : len(filePath)]

    return "// Generated from " + fileName + "\nconstexpr const char* " + variableName + " = " + contents

# Append the const char* string to the header file
def AppendConstCharToHeader(constChar : str):
    header.write("\n")
    header.write(constChar)
    header.write("\n")

for gen in gens:
    print("Generating constexpr const char* string for file: " + gen)
    lastIndex = gen.rfind("/")
    fileName = gen[lastIndex + 1 : len(gen)]
    typeIndex = fileName.rfind(".")
    fileStart = fileName[0 : typeIndex]
    fileType = fileName[typeIndex + 1 : len(fileName)]
    variableName = "generated_" + fileStart + "_" + fileType
    AppendConstCharToHeader(FileToConstChar(gen, variableName))

header.close()