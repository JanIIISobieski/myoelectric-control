#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 15:19:06 2019

@author: Gabriel Antoniak
"""

from keras.models import load_model
import numpy as np

class EMG_Decode():
    def __init__(self, model_to_import):
        self.emg = []
        self.model_string = model_to_import
        self.model = load_model(self.model_string)
        self.num_electrodes = 8
        self.rms = np.zeros(self.num_electrodes)
        self.prediction_categorical = []
        self.prediction = 0
        self.dictionary = {0: "rest",
                           1: "open hand",
                           2: "close hand",
                           3: "rotate wrist left",
                           4: "rotate wrist right",
                           5: "thumb up"}

    def get_RMS(self):
        self.rms = np.mean(self.emg, axis=1)
        self.rms = np.reshape(self.rms, (1, self.num_electrodes))

    def predict(self, emg):
        self.emg = np.asarray(emg)
        self.emg = np.reshape(self.emg, (1, self.emg.shape[0], self.emg.shape[1], 1))
        self.get_RMS()
        self.prediction_categorical = self.model.predict([self.emg, self.rms])
        self.prediction = np.argmax(self.prediction_categorical)
        print(self.prediction)
        #print(self.dictionary[self.prediction])