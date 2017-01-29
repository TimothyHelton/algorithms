#! /usr/bin/env python
# -*- coding: utf-8 -*-

""" Big O Notation Module

.. moduleauthor:: Timothy Helton <timothy.j.helton@gmail.com>
"""

import os.path as osp

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.misc as sci_msc


n = np.linspace(0.001, 4, 1000)
log_n = np.log(n)
n_log_n = n * log_n
n_squared = np.square(n)
n_factorial = sci_msc.factorial(n)

big_o = pd.DataFrame(np.c_[n, log_n, n_log_n, n_squared, n_factorial],
                     columns=['O(n)', 'O(log n)', 'O(n log n)',
                              'O($n^2$)', 'O(n!)'])

if __name__ == '__main__':
    fig, ax = plt.subplots(figsize=(10, 8), facecolor='white')
    fig.canvas.set_window_title('Big O Notation Common Performance Models')
    big_o.plot(ax=ax, kind='line', style=['--', '-', '-.', ':', '-'])
    for n in range(5):
        ax.lines[n].set_linewidth(2)
    ax.xaxis.set_ticks([])
    ax.yaxis.set_ticks([])
    plt.title('Big O Notation Common Performance Models', fontsize=24)
    plt.xlabel('n', fontsize=18)
    plt.grid()

    plt.show()
    # plt.savefig(osp.join('..', 'big_o_models.png'))
