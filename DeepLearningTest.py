# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 17:48:45 2019

@author: Emilie
"""

import mne
import numpy as np
import pandas as pd
#test = mne.io.read_raw_edf('test.edf')
test = mne.io.read_raw_edf('sbs2data_2018_09_01_08_04_51_328.edf')
print(test.info)

mne.viz.plot_raw(test, duration = 5, n_channels=14,bad_color='b')

Sleep(data='test.edf', hypno='myhypno.csv', use_mne=True).show()




mne.viz.plot_raw_psd(test,picks='P3',fmin=0.5,fmax=40, n_overlap=50)

mne.Epochs(test)

frequencies = np.arange(7, 30, 3)
power = mne.time_frequency.tfr_morlet(test, n_cycles=2, return_itc=False,
                                      freqs=frequencies, decim=3)
power.plot(['P3'])


test.ch_names['P3']

test.head()

#mne.viz.plot_topomap(test,times)

