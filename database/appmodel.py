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

class Abilities(BaseModel):
    '''
    I think "role" atribute is not needed coz we can use abilities to
    infer the role, if the ability is not attendant obviouosly is
    the teacher.
    '''
    id          = PrimaryKeyField()
    name        = CharField(unique=True, null=False)
    description = CharField(null=False)
    timestamp   = DateTimeField(default=datetime.datetime.now())

    def createAbility(name, description):
        Abilities.create(name=name, description=description)

class UsersAbilities(BaseModel):
    '''Same as Abilities class, roles are infered.
    '''
    id            = PrimaryKeyField()
    user          = ForeignKeyField(Users)
    ability       = ForeignKeyField(Abilities)
    rating_resume = IntegerField()
    cost          = IntegerField()
    timestamp     = DateTimeField(default=datetime.datetime.now())

class Events(BaseModel):
    '''All events are created here, you must have an attendant entry
    at least for the teacher in order to make it consistent
    '''
    id          = PrimaryKeyField()
    name        = CharField(null=False)
    description = CharField(null=False)
    date        = DateTimeField(null=False)
    city        = CharField(null=False)
    gps         = CharField()
    address     = CharField(null=False)
    status      = CharField(null=False) # not sure about this
    timestamp   = DateTimeField(default=datetime.datetime.now())


class ImgGallery(BaseModel):
    '''All media URIs must be stored here
    '''    
    id        = PrimaryKeyField()
    uri       = CharField(null=False)
    user      = ForeignKeyField(Users)
    event     = ForeignKeyField(Events)
    comment   = CharField()
    timestamp = DateTimeField(default=datetime.datetime.now())


class Attendants(BaseModel):
    '''
    Most important table, we cross all the important data here avoiding
    (n,m) relationships
    '''
    id        = PrimaryKeyField()
    user      = ForeignKeyField(Users)
    event     = ForeignKeyField(Events)
    ability   = ForeignKeyField(Abilities)
    timestamp = DateTimeField(default=datetime.datetime.now())

class Comments(BaseModel):
    '''Super simple comments related to the event by attendants
    '''
    id        = PrimaryKeyField()
    attendant = ForeignKeyField(Attendants)
    comment   = CharField(null=False)
    rating    = IntegerField(null=False)
    timestamp = DateTimeField(default=datetime.datetime.now())

TABLES = (Users, Abilities, UsersAbilities, Comments, Attendants, Events, ImgGallery)


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
        #Abilities.createAbility(name="test",description="description")
        print(type(BaseModel))
        
        print ("tables ",database.get_tables()) 
        sys.exit()