#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 15:19:06 2019

@author: Gabriel Antoniak
"""

import numpy as np

class EMG_Decode():
    def __init__(self, model_to_import):
        self.emg = []
        self.num_electrodes = 8
        self.rms = np.zeros(self.num_electrodes)
        self.mean = []
        self.prediction_categorical = []
        self.prediction = 0
        self.dictionary = {0: "rest",
                           1: "open hand",
                           2: "close hand",
                           3: "rotate wrist left",
                           4: "rotate wrist right",
                           5: "thumb up"}

    def get_means(self):
        self.rms = np.mean(self.emg, axis=1)
        self.rms = np.reshape(self.rms, (1, self.num_electrodes))
        self.mean = np.mean(self.rms)

    def predict(self, emg):
        self.emg = np.asarray(emg)
        self.emg = np.reshape(self.emg, (1, self.emg.shape[0], self.emg.shape[1], 1))
        self.get_means()

        if self.mean < 30:
            self.prediction = 0
        elif self.mean > 50 and np.argmax(self.rms) == 3:
            self.prediction = 1
        elif self.mean > 100 and np.argmax(self.rms) == 7:
            self.prediction = 2
        else:
            self.prediction = 5
        print(self.prediction)