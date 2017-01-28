#! /usr/bin/env python
# -*- coding: utf-8 -*-

""" Binary Search Algorithm Module

.. moduleauthor:: Timothy Helton <timothy.j.helton@gmail.com>
"""

import logging
import math
from typing import Tuple, Union


# Set Up Logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
date_format = '%m/%d/%Y %I:%M:%S'
log_format = ('%(asctime)s  %(levelname)8s  -> %(name)s <- '
              '(line: %(lineno)d) %(message)s\n')
formatter = logging.Formatter(fmt=log_format, datefmt=date_format)
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)


class BinarySearch:
    """Methods related to performing a binary search algorithm.

    :param item: item to be found
    :type: str | int | float
    :param values: all values to be searched
    :type: str | tuple | list | iter

    :Attributes:

        - **item**: *str | int | float* item to be found
        - **item_ids**: *int* index for the item to be found
        - **values**: *str | tuple | list | iter* all values to be \
            searched
        - **solution_steps**: *int* number of steps required to find item in \
            the set of values

    :Details:

    """
    def __init__(self,
                 item: Union[str, int, float]=None,
                 values: Union[str, set, tuple, list, iter]=None):
        self.item = item
        self.values = values
        self.item_idx = None

        try:
            self._low_idx = 0
            self._high_idx = len(self.values)
            self._med_idx = len(self.values) // 2
        except TypeError:
            logger.warning('The values argument was not provided.')
            self._low_idx = None
            self._high_idx = None
            self._med_idx = None

        self.steps = 0
        self.max_steps = None

    def __repr__(self) -> str:
        return "BinarySearch(item={}, values={})".format(self.item,
                                                         self.values)

    def calc_median(self):
        """Determine the median index."""
        try:
            self._med_idx = (self._low_idx + self._high_idx) // 2
        except TypeError:
            self.no_values()

    def calc_steps(self):
        """Determine the number of steps required to find the item."""
        try:
            self.max_steps = math.ceil(math.log2(len(self.values)))
        except TypeError:
            self.no_values()

    def find_index(self):
        """Find the index of the item in the argument of values."""
        self.steps += 1
        self.calc_median()
        med_value = self.values[self._med_idx]
        if med_value == self.item:
            self.item_idx = self._med_idx
        elif med_value > self.item:
            self._high_idx = self._med_idx - 1
            self.find_index()
        else:
            self._low_idx = self._med_idx + 1
            self.find_index()

    def find_item(self) -> Tuple[int, int, int]:
        """Notify the user of the item index and number of search steps.

        :returns: item index, actual number of search steps and maximum \
            possible number of search steps
        """
        self.steps = 0
        self.calc_steps()
        self.find_index()
        return self.item_idx, self.steps, self.max_steps

    @staticmethod
    def no_values():
        """Log that the values argument must be defined for current method."""
        logger.error('The argument "values" must be defined for this '
                     'method.')
