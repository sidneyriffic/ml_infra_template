#!/usr/bin/env python3
"""Command line entry point for data/model interactions"""


import importlib
import argparse
import preprocess_ex as ppex
print(ppex)


description = 'Define model and data operations'
parser = argparse.ArgumentParser(description)
parser.add_argument('-m', '--model', dest='make_model_path',
                    help='Model build path')
parser.add_argument('-p', '--preprocess', dest='pre_path',
                    help='Preprocess folder path')
parser.add_argument('-s', '--serialized', dest='serial_model',
                    help='Use a saved serialized model')
parser.add_argument('-t', '--train', dest='train_path',
                    help='Train a model')
args = parser.parse_args()
print(args)
pre_path = args.pre_path[1:-1]
preprocess = importlib.import_module(pre_path + '.preprocess')
print(preprocess)
preprocess.preprocess(pre_path + '/')
