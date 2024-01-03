import numpy as np
import pandas as pd


class Vandermonde():


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

        years_selected = years[-6:]
        populations_selected = populations[-6:]

        matrix = np.vander(
            x=years_selected,
            N=len(years_selected),
        )

        coefficients = np.linalg.solve(
            matrix,
            populations_selected
        )

        return np.polyval(
            coefficients,
            data_predicted
        )

