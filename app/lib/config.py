# -*- coding: utf-8 -*-
import os
import yaml

def read_config(filename):
    """
    @param filename: The file of configuration
    """
    with open(filename, 'r') as f:
        return yaml.load(f)

def get_config(filename="config.yml"):
    config = read_config(os.path.join(os.path.dirname(__file__), '..', filename))
    return config

