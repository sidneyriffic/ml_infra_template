#!/usr/bin/env python3
"""
Model note heres. This is a very simple model with just 1 dense node
that takes the Titanic ages as input and outputs labels.
"""


import tensorflow as tf
keras = tf.keras


def model(inputs, labels):
    """Take inputs, feed through dense layer, output survival prediction"""
