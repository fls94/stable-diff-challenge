# coding: utf-8
"""

"""
import json


def load_config(path):
    """

    """

    conf_file = open(path, 'r')
    conf = json.load(conf_file)
    return conf
