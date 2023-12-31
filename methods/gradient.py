import numpy as np
import pandas as pd


class Gradient():

    @staticmethod
    def calcule(
            populations:np.ndarray, 
            years:np.ndarray, 
            data_predicted:np.ndarray
        ):
        '''
            This method is designed to calculate the gradient predictions

            Args:
                populations: A numpy array with the populations data
                years: A numpy array with the years data
        '''
        r = pow(populations[-1] / populations[0], 1 / (years[-1] - years[0])) - 1

        new_population =  populations[0] * pow(r + 1, (data_predicted - years[0]))


        return new_population
