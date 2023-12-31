import numpy as np
import pandas as pd
from scipy.optimize import curve_fit


class Logistic():

    @staticmethod
    def calcule(
            populations:np.ndarray, 
            years:np.ndarray, 
            data_predicted:np.ndarray
        ):
        '''
            This method is designed to calculate the logistic predictions

            Args:
                populations: A numpy array with the populations data
                years: A numpy array with the years data
        '''
        def modelo_logistic(t, M, k, c):
            '''
                Schema for the model logistic
            '''
            return M / (1 + k * np.exp(-c * t))


        popt, pcov = curve_fit(modelo_logistic, years, populations)
    
        new_population = modelo_logistic(data_predicted, *popt)

        return new_population