#! /usr/bin/env python
# -*- coding: utf-8 -*-

""" Statistics Module

.. moduleauthor:: Timothy Helton <timothy.j.helton@gmail.com>
"""

import numpy as np


class General:
    """Class to calculate general statistical properties of a data set.

    :param ndarray data: data set

    :Attributes:

    - **data**: *ndarray* initial data set
    - **mean**: *float* the mean of

    """
    def __init__(self, data=None):
        self.data = data
        self.mean = None
        self.median = None
        self.median_low = None
        self.median_high = None

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
