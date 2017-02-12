import os, sys
'''
This module allows to cross importing from the root app directory
'''
sys.path.insert(0, os.path.abspath(__file__+'/../..'))
