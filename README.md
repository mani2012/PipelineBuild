# PipelineBuild
Generates commands for analyzing all the files in the given directory.

Python program that given a directory with input files, creates a file with commands for analyzing the files, which can then be given as input to SplitQsub program for generating qsub files.


#### 1. Running

1.1 Prerequisite: Need to have python 2.7.3 or later version installed and add python to your PATH variable (Usually already done as part of python installation)
    
1.2 Change directory to where you downloaded the code 

1.3 Simply run `python setup.py install` if you want to install globally or  
simply run `python setup.py install --user` if you want to install for the local user.  
If you have never installed another python module before or you do not have python setuptools  
simply run `python install.py`, which will use ez_setup.py to bootstrap the right version of the package installer tooling for you.

1.4 For usage information, simply run `pipelinebuild -h` after installation as above or  
simply run `python pipelinebuild/pipeline_build.py -h` if you want to try without installing.


```{r}
usage: pipeline_build.py [-h] [--version] -commandsFile CMD_FILE
                        [-inputDir INPUTDIR] 
                        [-file1Pattern FILE1_PATTERN]
                        [-file2Pattern FILE2_PATTERN] 
                        [-outDir OUTDIR]
                        [-outFile OUTFILE]

optional arguments:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  -commandsFile CMD_FILE
                        Template Commands File that has the commands to be
                        generated for each sample file
  -inputDir INPUTDIR    Input Directory where the files to be analyzed are
                        located (Default=. (current directory))
  -file1Pattern FILE1_PATTERN
                        File1 matching pattern (default: .R1.fastq.gz)
  -file2Pattern FILE2_PATTERN
                        File2 matching pattern (default: .R2.fastq.gz)
  -outDir OUTDIR        Output Directory (Default=. (current directory))
  -outFile OUTFILE      Output File name (Default=pipeline_commands.sh
                        (current directory))

```

####  2. Support and Contact

PipelineBuild is developed by Solaiappan Manimaran.

Department of Biostatistics  
School of Public Health  
Boston University  
801 Massachusetts Avenue 3rd Floor  
Boston, MA 02118  

