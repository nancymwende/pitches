import unittest
from app.models import Comment


class TestComment(unittest.TestCase):
    def setUp(self):
        self.new_comment = Comment(
            id=408765, body='Add a comment', author_id='mwende', post_id=1234)

    def tearDown(self):
        Comment.query.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment, Comment))