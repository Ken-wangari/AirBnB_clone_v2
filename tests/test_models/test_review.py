#!/usr/bin/python3
"""Test module for Review class"""
import unittest
from models.review import Review
from tests.test_models.test_base_model import test_basemodel


class test_review(test_basemodel):
    """Test cases for Review class"""

    def __init__(self, *args, **kwargs):
        """Initialize TestReview"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """Test place_id attribute"""
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """Test user_id attribute"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """Test text attribute"""
        new = self.value()
        self.assertEqual(type(new.text), str)


if __name__ == "__main__":
    unittest.main()

