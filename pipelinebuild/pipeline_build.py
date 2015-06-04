#!/usr/bin/env python
# Author: Solaiappan Manimaran
# Generates commands for analyzing all the files in the given directory

#usage information: pipelineBuild.py -h

#       PipelineBuild 1.0 - Python program that given a directory with input files 
#       creates a file with commands for analyzing the files, 
#       which can then be given as input to SplitQsub program for generating qsub files
#       Copyright (C) 2015  Solaiappan Manimaran
#
#       This program is free software: you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation, either version 3 of the License, or
#       any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os, fnmatch, re, argparse

def generateCommands(inputArgs):
    files1 = []
    files2 = []
    of = inputArgs.outdir + os.path.sep + inputArgs.outfile
    with open(of,'w') as out1:
        for root, _, filenames in os.walk(inputArgs.inputdir):
            for filename in fnmatch.filter(filenames, '*'+inputArgs.file1_pattern):
                files1.append(os.path.join(root, filename))
            for filename in fnmatch.filter(filenames, '*'+inputArgs.file2_pattern):
                files2.append(os.path.join(root, filename))
        count = 0
        for f1 in files1:
            with open(inputArgs.cmd_file,'r') as in1:
                for ln in in1:
                    if "@@FILE1@@" in ln:
                        ln = ln.replace("@@FILE1@@", f1)
                    if len(files2) > count:
                        if "@@FILE2@@" in ln:
                            ln = ln.replace("@@FILE2@@", f1)
                    if "@@FILE1MATCH@@" in ln:
                        fname = os.path.split(f1)[1]
                        f1match = re.split(inputArgs.file1_pattern, fname)[0]
                        ln = ln.replace("@@FILE1MATCH@@", f1match)
                    out1.write(ln)



parser = argparse.ArgumentParser(description="PipelineBuild")

# create the top-level parser
parser.add_argument('--version', action='version', version='%(prog)s 1.0')
parser.add_argument('-commandsFile', action='store', dest='cmd_file', required=True, 
    help='Template Commands File that has the commands to be generated for each sample file')
parser.add_argument('-inputDir', action='store', default='.', dest='inputdir',
    help='Input Directory where the files to be analyzed are located (Default=. (current directory))')
parser.add_argument('-file1Pattern', action='store', dest='file1_pattern', required=False, 
    default="R1.fastq.gz", help='File1 matching pattern (default: R1.fastq.gz)')
parser.add_argument('-file2Pattern', action='store', dest='file2_pattern', required=False, 
    default="R2.fastq.gz", help='File2 matching pattern (default: R2.fastq.gz)')
parser.add_argument('-outDir', action='store', default='.', dest='outdir',
    help='Output Directory (Default=. (current directory))')
parser.add_argument('-outFile', action='store', default='pipeline_commands.sh', dest='outfile',
    help='Output File name (Default=pipeline_commands.sh (current directory))')

inputArgs = parser.parse_args()
generateCommands(inputArgs)
