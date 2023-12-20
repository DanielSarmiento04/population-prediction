import numpy as np
import pandas as pd



class Linear():

    @staticmethod
    def calcule(
            populations:np.ndarray, 
            years:np.ndarray, 
            data_predicted:np.ndarray
        ):
        '''
            This method is designed to calculate the linear predictions

            Args:
                populations: A numpy array with the populations data
                years: A numpy array with the years data
        '''

        r = (populations[-1] - populations[0] ) / (years[-1] - years[0])

        new_population = populations[0] + (r) * (data_predicted - years[0])

        return new_population

