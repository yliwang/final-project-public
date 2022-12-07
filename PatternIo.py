import sys
import  os

import numpy as np

#return 1 on success,
# 0 otherwise
def PreparePatterns( PatDir, #patterns stored in sub-dirs, PatDir is the parent folder to all of the sub-dirs 
    PatFile,    #resulting pattern file in the binary format described in the document file including path
    LblFile ): #resulting label file. also in the binary format as specified in the document file.

    return 1


#return 1 on success,
# 0 otherwise
def SplitPatterns( PatFile, # pattern file in the binary format described in the document
    LblFile,    # label file.
    TrainPatFile, # where to put the patterns in training group
    TrainLblFile, # labels for the training patterns
    TestPatFile,    # where to put the patterns in the test group
    TestLblFile,   # labels for the test patterns
    percent): # how many patterns will be assigned to training group, in the format for example 0.70,
    # means 70 percent of the patterns will be assigned to training group


    return 1


def LoadPatterns( PatFile, #pattern file in the binary format described in the word document.    
    LblFile ): #label file



    
    return pats, lbls # this the read patterns, and lbls
                # patterns are in format [numbers][75*100] as a numpy array
                # labels are also in a 1-D numpy array
