#! /usr/bin/env python
# -*- coding: utf-8 -*-

""" Binary Search Algorithm Test Module

.. moduleauthor:: Timothy Helton <timothy.j.helton@gmail.com>
"""

import pytest
import testfixtures as tf

from algorithms import search

#######################################
# Test BaseSearch Class
# Test BaseSearch.log_n()
log_n = {
    'str': (list('abcdefge'), 3),
    'tuple': (tuple(range(8)), 3),
    'list': (list(range(8)), 3),
    'iter': (range(8), 3),
    'round_up': (range(100), 7),
    'none': (None, None),
}


@pytest.mark.parametrize('values, expected',
                         list(log_n.values()),
                         ids=list(log_n.keys()))
def test__base_log_n(values, expected):
    inst = search.BaseSearch(values=values)
    inst.log_n()
    assert inst.max_steps == expected


def test__base_log_n_logger():
    with tf.LogCapture() as log:
        inst = search.BaseSearch()
        inst.log_n()
    log.check(
        ('algorithms.search', 'ERROR',
         'The argument "values" must be defined for this method.'),
    )


# Test BaseSearch.no_values()
def test__base_no_values():
    with tf.LogCapture() as log:
        search.BaseSearch().no_values()
    log.check(
        ('algorithms.search', 'ERROR',
         'The argument "values" must be defined for this method.'),
    )


#######################################
# Test BinarySearch Class
# Test BinarySearch.__repr__()
repr_tests = {
    'default': ({}, 'item=None, values=None'),
    'ints': ({'item': 5, 'values': [1, 2, 3, 4, 5]},
             'item=5, values=[1, 2, 3, 4, 5]'),
    'strs': ({'item': 'a', 'values': 'abc'},
             'item=a, values=abc'),
    'floats': ({'item': 3.3, 'values': [1.1, 2.2, 3.3]},
               'item=3.3, values=[1.1, 2.2, 3.3]'),
}


@pytest.mark.parametrize('kwargs, expected',
                         list(repr_tests.values()),
                         ids=list(repr_tests.keys()))
def test__binary_repr(kwargs, expected):
    inst = search.BinarySearch(**kwargs)
    assert inst.__repr__() == 'BinarySearch({})'.format(expected)


# Test BinarySearch.calc_median()
calc_median = {
    'even_div': (range(10), 5, 5),
    'odd_div': (range(11), 5, 5),
}


@pytest.mark.parametrize('values, expected_idx, expected_value',
                         list(calc_median.values()),
                         ids=list(calc_median.keys()))
def test__binary_calc_median(values, expected_idx, expected_value):
    inst = search.BinarySearch(values=values)
    inst.calc_median()
    assert inst._med_idx == expected_idx
    assert inst.calc_median() == expected_value


def test__binary_calc_median_logger():
    with tf.LogCapture() as log:
        search.BinarySearch().calc_median()
    log.check(
        ('algorithms.search', 'WARNING',
         'The values argument was not provided.'),
        ('algorithms.search', 'ERROR',
         'The argument "values" must be defined for this method.'),
    )


# Test BinarySearch.search()
find_item = {
    'incremental': ({'item': 4, 'values': range(10)}, 4),
    'steps': ({'item': 15, 'values': range(5, 50, 5)}, 2),
    'str': ({'item': 'c', 'values': list('abcdefg')}, 2),
}


@pytest.mark.parametrize('kwargs, expected',
                         list(find_item.values()),
                         ids=list(find_item.keys()))
def test__binary_find_item(kwargs, expected):
    inst = search.BinarySearch(**kwargs)
    assert inst.search()[0] == expected
