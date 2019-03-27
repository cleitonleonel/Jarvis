#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import os


def speek(rand):
    phrase = str(random.choice(rand))
    os.system('espeak -vpt-br -k -20 ' + '"' + phrase + '"')
