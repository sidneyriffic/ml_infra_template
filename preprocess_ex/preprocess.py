#!/usr/bin/env python3
"""
Preprocessing notes here. This is a very simple Titanic preprocess that
only keeps the age. Output files should be saved in this folder.
"""


import tensorflow as tf
import tensorflow_datasets as tfds
import numpy as np


def preprocess(path):
    """Run preprocess on Titanic tfds to keep only age."""
    tf.compat.v1.enable_eager_execution()
    titanic = tfds.load('Titanic', split='train')
    print(titanic)
    labels = []
    ages = []
    for sample in titanic.take(1):
        ages.append(sample['features']['age'].numpy())
        labels.append(sample['survived'].numpy())
    np.save(path + 'ages.npy', np.asarray(ages))
    np.save(path + 'labels.npy', np.asarray(labels))
