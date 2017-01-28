#! /usr/bin/env python
# -*- coding: utf-8 -*-

""" Binary Search Algorithm Test Module

.. moduleauthor:: Timothy Helton <timothy.j.helton@gmail.com>
"""

import pytest
import testfixtures as tf

from algorithms import search_binary as sb


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
def test__bs_repr(kwargs, expected):
    inst = sb.BinarySearch(**kwargs)
    assert inst.__repr__() == 'BinarySearch({})'.format(expected)


# Test BinarySearch.calc_steps()
calc_steps = {
    'str': (list('abcdefge'), 3),
    'tuple': (tuple(range(8)), 3),
    'list': (list(range(8)), 3),
    'iter': (range(8), 3),
    'round_up': (range(100), 7),
    'none': (None, None),
}


@pytest.mark.parametrize('values, expected',
                         list(calc_steps.values()),
                         ids=list(calc_steps.keys()))
def test__bs_calc_steps(values, expected):
    inst = sb.BinarySearch(values=values)
    inst.calc_steps()
    assert inst.max_steps == expected


def test__bs_calc_steps_logger():
    with tf.LogCapture() as l:
        inst = sb.BinarySearch()
        inst.calc_steps()
    l.check(('algorithms.search_binary', 'WARNING',
             'The values argument was not provided.'),
            ('algorithms.search_binary', 'ERROR',
             'The argument "values" must be defined for this method.'))


# Test BinarySearch.find_item()
find_item = {
    'incremental': ({'item': 4, 'values': range(10)}, 4),
    'steps': ({'item': 15, 'values': range(5, 50, 5)}, 2),
    'str': ({'item': 'c', 'values': list('abcdefg')}, 2),
}


@pytest.mark.parametrize('kwargs, expected',
                         list(find_item.values()),
                         ids=list(find_item.keys()))
def test__bs_find_item(kwargs, expected):
    inst = sb.BinarySearch(**kwargs)
    assert inst.find_item()[0] == expected


# Test BinarySearch.no_values()
def test__bs_no_values():
    with tf.LogCapture() as l:
        sb.BinarySearch().no_values()
    l.check(('algorithms.search_binary', 'WARNING',
             'The values argument was not provided.'),
            ('algorithms.search_binary', 'ERROR',
             'The argument "values" must be defined for this method.'))
