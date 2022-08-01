# test_db.py

import unittest
from peewee import *
from app import TimelinePost

MODELS = [TimelinePost]

# use an in-memory SQLite for tests.
test_db = SqliteDatabase(':memory:')

class TestTimelinePost(unittest.TestCase):
    def setUp(self):
        # Bind models classes to test db. Since we have a complate list of 
        # all models, we don't need to recursively bind dependencies
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)

        test_db.connect()
        test_db.create_tables(MODELS)

    def tearDown(self):
        # Not strictly neccesary since SQLite in-memory databases only live
        # for the duration of the connection, and in the next step we close
        # the connection...but a good practice all the same.
        test_db.drop_tables(MODELS)

        # Close connection to do.
        test_db.close()

    def test_timeline_post(self):
        # Create 2 Practice Posts.
        first_post = TimelinePost.create(name='John Doe', email='john@example.com', content='Hello World, I\'m John!')
        assert first_post.id == 1
        second_post = TimelinePost.create(name='Jane Doe', email='jane@example.com', content='Hello world, I\'m Jane!')
        assert second_post.id == 2
        first_post_data = TimelinePost.select().where(TimelinePost.id == 1).get()
        assert first_post_data.name == "John Doe"
        assert first_post_data.email == "john@example.com"
        assert first_post_data.content == "Hello World, I\'m John!"
        second_post_data = TimelinePost.select().where(TimelinePost.id == 2).get()
        assert second_post_data.name == "Jane Doe"
        assert second_post_data.email == "jane@example.com"
        assert second_post_data.content == "Hello world, I\'m Jane!"

