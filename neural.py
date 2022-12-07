import sys
import numpy as np

import pickle # used to load and store trained nn

def sigmoid(x):
    return 1./(1.+np.exp(-x))


class NeuralNetwork:
    def __init__( self,
                NumInput,
                NumHidden,
                NumOutput,
                LearningRate ):
        self.input = NumInput
        self.hidden = NumHidden
        self.output = NumOutput
        self.LearningRate = LearningRate

        # input to hidden layer 
        # complete this part 

        # end of complete this part


    def TrainATime( self, #reference to us
        x,  # is one input vector
        y ): # it label for this input vector, in one-hot format


        return 
   

    def RunATime( self, # reference to us
    x ):        # is one input vector
        O = None    #to supress syntax error, O is initialzed with None


        # return the output for this input
        return O


    def Evaluate( self, # reference to us
        feas,           #input feature vectors, can be many
        labels):        # input labels for the feature vectors, in one-hot 
        return corrects, wrongs # corrects contain number of correctly classified feas,
                                # wrongs, number of errorly classified.

    # training interface
    def Train( self, 
        feas,       #feature vectors used for training
        labels,     # corresponding labels for the feature vectors
        epochs ):   # how many epochs to train, an epoch means training the nn 
                    # with all feature vectors once. 

        #!call TrainATime to train           
        #!TrainATime( ------)
        

        #!call Eavluate to see how well we are now at
        #!corrects, wrongs = Evaluate( nn, feas, labels )
        prec = corrects/(corrects+wrongs)
        print( "epoch: ", i, "precision: %.5f" % prec )

    #inference interface
    def Run( self, # reference to us
        feas ):    #feature vectors 

        #will return the classification results in res
        return res

    #store the trained nn to a specified file, using pickle
    #on success, return 1
    #0 otherwise.
    def Save( self, 
        obj_file):      #file name including path

        return 1

    #load nn from file
    #on success, return 1
    #0 otherwise.    
    def Load( self, 
        obj_file ):

        return 1

