#! /usr/bin/env python
# -*- coding: utf-8 -*-

""" Statistics Test Module

.. moduleauthor:: Timothy Helton <timothy.j.helton@gmail.com>
"""

from collections import namedtuple

import numpy as np
import pytest

from algorithms import stats


###############################################################################
# Test General Class
# Test __repr__()
def test__general_repr():
    inst = stats.General()
    assert inst.__repr__() == 'General(data=None)'


# Test calc_mean()
calc_mean = {'positive': ({'data': np.arange(3)}, 1),
             'negative': ({'data': np.arange(3) * -1}, -1),
             'zero': ({'data': np.zeros(3)}, 0),
             'unordered': ({'data': np.array([2, 0, 1])}, 1),
             }


@pytest.mark.parametrize('kwargs, expected',
                         list(calc_mean.values()),
                         ids=list(calc_mean.keys()))
def test__general_calc_mean(kwargs, expected):
    inst = stats.General(**kwargs)
    inst.calc_mean()
    assert inst.mean == expected


# Test calc_median()
calc_median = {'even': ({'data': np.arange(4)}, 1.5, np.arange(2),
                        np.arange(2, 4, 1)),
               'odd': ({'data': np.arange(5)}, 2, np.arange(2),
                       np.arange(3, 5, 1)),
               'small_odd': ({'data': np.arange(3)}, 1, 0, 2),
               'small_even': ({'data': np.arange(2)}, 0.5, 0, 1),
               'single': ({'data': np.arange(1)}, 0, None, None),
               'unordered': ({'data': np.array([2, 0, 1, 4, 3])}, 2,
                             np.arange(2), np.arange(3, 5, 1)),
               }


@pytest.mark.parametrize('kwargs, median, low_array, high_array',
                         list(calc_median.values()),
                         ids=list(calc_median.keys()))
def test__general_calc_median(kwargs, median, low_array, high_array):
    inst = stats.General(**kwargs)
    inst.calc_median()
    assert inst.median == median
    assert np.all(np.equal(inst.median_low, low_array))
    assert np.all(np.equal(inst.median_high, high_array))


# Test calc_quartiles()
Quartiles = namedtuple('Quartiles', ('q1', 'q2', 'q3'))
quartiles = {'odd': ({'data': np.arange(7)}, Quartiles(1, 3, 5), 4),
             'even': ({'data': np.arange(6)}, Quartiles(1, 2.5, 4), 3),
             'repeat': ({'data': np.array([3, 7, 8, 5, 12, 14, 21, 15, 18,
                                          14])},
                        Quartiles(7, 13, 15), 8),
             }


@pytest.mark.parametrize('kwargs, quartile_tuple, inner_quartile_range',
                         list(quartiles.values()),
                         ids=list(quartiles.keys()))
def test__calc_quartiles(kwargs, quartile_tuple, inner_quartile_range):
    inst = stats.General(**kwargs)
    inst.calc_quartiles()
    assert inst.quartiles == quartile_tuple
    assert inst.inner_quartile_range == inner_quartile_range
