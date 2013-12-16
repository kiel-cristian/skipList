#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Node(object):
    def __init__(self, parent, key):
        #Se mantiene referencia al padre para las rotaciones
        self.parent = parent
        self.left  = None
        self.right = None
        self.key   = key