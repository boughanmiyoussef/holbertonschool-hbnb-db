#!/usr/bin/python3
"""SQLAlchemyDataManagerTestCase"""
import unittest
from persistence.data_manager import DataManager
from persistence.database import db, app
from .test_persistence_manager import PersistenceManagerTestCase

class SQLAlchemyDataManagerTestCase(PersistenceManagerTestCase, unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['TESTING'] = True
        db.create_all()
        cls.persistence_manager = DataManager()

    @classmethod
    def tearDownClass(cls):
        db.session.remove()
        db.drop_all()

if __name__ == '__main__':
    unittest.main()