#!/usr/bin/env python
#  coding: utf-8

from peewee import *
import datetime
import sqlite3

DATABASE = 'test.db'
database = SqliteDatabase(DATABASE, threadlocals=True)
