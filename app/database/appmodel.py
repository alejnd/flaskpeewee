#!/usr/bin/env python
#  coding: utf-8

from peewee import *
import datetime
import sqlite3
from playhouse.signals import Model as SignalModel #This is needed for signal support aka triggers
from config import config
import os

DATABASE = config.DATABASE
database = SqliteDatabase(DATABASE, threadlocals=True)

class BaseModel(SignalModel):
    class Meta:
        database = database

class Users(BaseModel):
    '''
    No real explanation needed, used to store users data
    '''
    id          = PrimaryKeyField()
    email       = CharField(unique=True)
    password    = CharField(null=False)
    username    = CharField(null=False, unique=True)
    name        = CharField(null=True)
    surname     = CharField(null=True)
    gender      = BooleanField(null=True)
    description = CharField(null=True)
    city        = CharField(null=True)
    status      = CharField(default='inactive') #active, inactive, verifying ...
    verified    = BooleanField(default=False)
    timestamp   = DateTimeField(default=datetime.datetime.now())
    update      = DateTimeField(null=True)

#--- Flask required methods ---
    def is_authenticated(self):
        return True

    def is_active(self):
        if self.status != 'inactive': return True
        else: return False

    def is_anonymous(self):
        return False

    def get_id(self):
        return (self.id)

TABLES = (Users,)

def create_tables():
    try: database.connect()
    except Exception as e: print(e)

    print("Creating database ", DATABASE)
    for table in TABLES:
        try: database.create_tables([table], safe= True)
        except Exception as e: print(e)

def delete_database():
    print ("Deleting database", DATABASE)
    try: os.remove(DATABASE)
    except Exception as e: print(e)


if __name__ == '__main__':
    import sys

    if len(sys.argv) == 1: sys.exit()
    if sys.argv[1] == 'createdatabase': create_database()
    elif sys.argv[1] == 'deletedatabase': delete_database()
    else: 
        print(type(BaseModel))
        
        print ("tables ",database.get_tables()) 
        sys.exit()