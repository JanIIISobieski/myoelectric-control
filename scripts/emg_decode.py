#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 15:19:06 2019

@author: Gabriel Antoniak
"""

import keras
from keras.models import load_model

import numpy as np
import pywt

first_level = 108
second_level = 62
third_level = 39
wavelet_length = first_level + second_level + 2*third_level

class EMG_Decode():
    def __init__(self, model_to_import):
        self.emg = []
        self.model_string = model_to_import
        self.model = load_model(self.model_string)
        self.num_electrodes = 8
        self.wavelet_coeffs = np.zeros((self.num_electrodes, wavelet_length))
        self.rms = np.zeros(self.num_electrodes)
        self.prediction = []

    def get_wavelet_coeffs(self):
        num = 0
        for electrodes in self.emg.T:
            cA3, cD3, cD2, cD1 = pywt.wavedec(electrodes, wavelet='db9',
                                              mode='zero', level=3)
            self.wavelet_coeffs[num, :] = np.concatenate((cD1, cD2, cD3, cA3))
            num += 1
        self.wavelet_coeffs = self.wavelet_coeffs.reshape((1, 248, 8, 1))

    def get_RMS(self):
        self.rms = np.sqrt(np.mean(np.square(self.emg), axis=0))
        self.rms = self.rms.reshape(1, self.num_electrodes)

    def predict(self, emg):
        self.emg = np.asarray(emg)
        self.get_wavelet_coeffs()
        self.get_RMS()
        self.predicted = self.model.predict([self.wavelet_coeffs, self.rms])

        self.wavelet_coeffs = np.zeros((self.num_electrodes, wavelet_length))
        self.rms = np.zeros(self.num_electrodes)