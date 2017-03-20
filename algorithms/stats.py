#! /usr/bin/env python
# -*- coding: utf-8 -*-

""" Statistics Module

.. moduleauthor:: Timothy Helton <timothy.j.helton@gmail.com>
"""

from collections import namedtuple

import numpy as np


class General:
    """Class to calculate general statistical properties of a data set.

    :param ndarray data: data set

    :Attributes:

    - **data**: *ndarray* initial data set
    - **mean**: *float* mean of data
    - **median**: *float* median of data
    - **median_low**: *ndarray* bottom half values of data (bottom 50%)
    - **median_high**: *ndarray* top half values of data (top 50%)
    - **quartiles**: *namedtuple* quartiles q1: 25%, q2: 50% (median), q3:75%
    - **quartile_range**: *float* middle 50% of data (q3 - q1)
    """
    def __init__(self, data=None):
        self.data = data
        self.mean = None
        self.median = None
        self.median_low = None
        self.median_high = None
        self.quartiles = None
        self.inner_quartile_range = None

    def __repr__(self):
        return f'General(data={self.data})'

    def calc_mean(self):
        """Calculate the mean of the data."""
        self.mean = self.data.sum() / self.data.shape

    def calc_median(self):
        """Calculate the median of the data."""
        if self.data.shape[0] is 1:
            self.median = self.data[0]
            self.median_low = None
            self.median_high = None

        data = np.sort(self.data.copy())
        length = data.shape[0]
        middle = length // 2
        if length % 2 is 0:
            self.median = data[middle - 1: middle + 1].sum() / 2
            self.median_low = data[:middle]
            self.median_high = data[middle:]
        else:
            self.median = data[middle]
            self.median_low = data[:middle]
            self.median_high = data[middle + 1:]

    def calc_quartiles(self):
        """Calculate the quartiles q1, q2, q3 and the quartile range."""
        Quartiles = namedtuple('Quartiles', ('q1', 'q2', 'q3'))
        original_data = self.data

        self.calc_median()
        q2 = self.median
        low_array = self.median_low
        high_array = self.median_high

        self.data = low_array
        self.calc_median()
        q1 = self.median

        self.data = high_array
        self.calc_median()
        q3 = self.median

        self.quartiles = Quartiles(q1, q2, q3)
        self.inner_quartile_range = q3 - q1

        self.data = original_data
