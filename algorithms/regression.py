#! /usr/bin/env python
# -*- coding: utf-8 -*-

""" Regression Module

.. moduleauthor:: Timothy Helton <timothy.j.helton@gmail.com>
"""

import os.path as osp

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import seaborn


class LeastSquares:
    """Least Squares Linear Regression

    :param ndarray x: x values
    :param ndarray y: y values

    :Attributes:

    - **slope**: *float* slope of regression line
    - **x**: *ndarray* x values
    - **y**: *ndarray* y values
    - **y_intercept**: *float* value where regression line intercepts y-axis
    """
    def __init__(self, x: np.ndarray, y: np.ndarray):
        self.x = x
        self.y = y
        self.slope = None
        self.y_intercept = None

    def __repr__(self) -> str:
        return f'LeastSquares(x={self.x}, y={self.y})'

    def calc_slope(self):
        """Calculate the slope

        slope = r * sigma_y / sigma_x

        r: Pearson Correlation
        sigma_x: standard deviation of x
        sigma_y: standard deviation of y
        """
        sigma_x = np.std(self.x)
        sigma_y = np.std(self.y)
        if sigma_x == 0 or sigma_y == 0:
            self.slope = 0
        else:
            r = np.corrcoef(x=self.x, y=self.y)[1, 0]
            self.slope = r * sigma_y / sigma_x

    def calc_y_intercept(self):
        """Calculate the y-intercept

        y_intercept = y_mean - slope * x_mean
        """
        if self.slope is None:
            self.calc_slope()

        x_mean = np.mean(self.x)
        y_mean = np.mean(self.y)
        self.y_intercept = y_mean - self.slope * x_mean

    def check_values(self) -> str:
        """Use SciPy to check the regression coefficients."""
        slope, intercept, r_value, p_value, std_err = stats.linregress(self.x,
                                                                       self.y)
        return ('\n\nCheck Values from SciPy\n\n'
                f'Slope: {slope:.2}\n'
                f'Intercept: {intercept:.2}')

    def plot_data(self, save_name=None, **kwargs):
        """Plot the data with regression line."""
        self.calc_slope()
        self.calc_y_intercept()

        fig = plt.figure('Least Squares Linear Regression', figsize=(5, 8),
                         facecolor='white', edgecolor='black')
        ax = plt.subplot2grid((1, 1), (0, 0))

        ax.scatter(self.x, self.y)

        regression_x = np.linspace(np.min(self.x), np.max(self.x), 100)
        regression_y = self.slope * regression_x + self.y_intercept
        ax.plot(regression_x, regression_y, '-b',
                label=f'Y = {self.slope:.2}X + {self.y_intercept:.2}')

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        plt.legend()
        plt.suptitle('Least Squares Linear Regression', fontsize=24)

        if save_name:
            name = osp.realpath(save_name)
            plt.savefig(name, **kwargs)
        else:
            plt.show()
