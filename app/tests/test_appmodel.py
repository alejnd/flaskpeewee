
#Use green command to run a nicer test output from test directory

import context
from config import TestingConfig
import unittest
import server
import time
from peewee import *

necessary_tables =set([ 'users'])

class DatabaseTests(unittest.TestCase):

    def setUp(self):
        server.app.config.from_object(TestingConfig)
        server.db.create_tables()

    def tearDown(self):
        server.db.delete_database()

    def test_check_all_tables_exist(self):
        assert set(server.db.database.get_tables()) == necessary_tables


class EndpointsTest(unittest.TestCase):

    def setUp(self):
        server.app.config.from_object(TestingConfig)
        server.db.create_tables()
        self.app = server.app.test_client()

    def tearDown(self):
        server.db.delete_database()

    def test_home_up(self):
        rv = self.app.get('/')
        assert rv.status_code == 200
    
    def test_register_login(self):
        rv = self.app.post('/register', data=dict(username='dummy',password='passpass',email='dummy@dumbmail.com'))
        assert rv.status_code == 200
        
        #print (rv.data)
    def test_valid_login(self):
        self.test_register_login()    
        rv = self.app.post('/login', data=dict(username='dummy', password='passpass'))
        assert rv.status_code == 200

    def test_unauthorized_login(self):
        rv = self.app.post('/login', data=dict(username='badguy', password='badpass'))
        assert rv.status_code == 401


if __name__ == '__main__':
    unittest.main()
