#! /usr/bin/env python
# -*- coding: utf-8 -*-

""" Regression Test Module

.. moduleauthor:: Timothy Helton <timothy.j.helton@gmail.com>
"""

import numpy as np
import pytest

from algorithms import regression


x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([10, 11, 12, 13, 14, 15])


###############################################################################
# Test LeastSquares Class
# Test LeastSquares.__repr__()
def test__leastsquares_repr():
    inst = regression.LeastSquares(x=x, y=y)
    assert inst.__repr__() == ('LeastSquares(x=[0 1 2 3 4 5], '
                               'y=[10 11 12 13 14 15])')

# Test LeastSquares.calc_slope()
calc_slope = {
    'zero': ({'x': np.arange(3), 'y': np.ones(3)}, 0),
    'pos': ({'x': np.arange(3), 'y': np.linspace(2, 6, 3)}, 2),
    'neg': ({'x': np.arange(3), 'y': -1 * np.linspace(2, 6, 3)}, -2),
}


@pytest.mark.parametrize('kwargs, expected',
                         list(calc_slope.values()),
                         ids=list(calc_slope.keys()))
def test__leastsquares_calc_slope(kwargs, expected):
    inst = regression.LeastSquares(**kwargs)
    inst.calc_slope()
    assert inst.slope == expected


# Test LeastSquares.calc_y_intercept()
y_int = {
    'zero': ({'x': np.arange(3), 'y': np.arange(3)}, 0),
    'pos': ({'x': np.arange(3), 'y': np.linspace(2, 6, 3)}, 2),
    'neg': ({'x': np.arange(3), 'y': -1 * np.linspace(2, 6, 3)}, -2),
}


@pytest.mark.parametrize('kwargs, expected',
                        list(y_int.values()),
                        ids=list(y_int.keys()))
def test__leastsquares_calc_y_intercept(kwargs, expected):
    inst = regression.LeastSquares(**kwargs)
    inst.calc_y_intercept()
    assert inst.y_intercept == expected


# Test LeastSquares_plot_data()
def test__leastsquares_plot_data():
    inst = regression.LeastSquares(x=np.arange(5), y=np.arange(5))
    inst.plot_data()
