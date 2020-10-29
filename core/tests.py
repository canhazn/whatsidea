from django.test import TestCase
from django.contrib.auth.models import User
from core import models



class TestModel(TestCase):

    def test_create_user(self):
        """Test creatng user""" 

        user = User.objects.create_user("testusername", "test@gmail.com", "123456")        
        self.assertEqual(user.username, "testusername")

    def test_create_idea_withow_user(self):
        """Test creating post withow user will false"""

        post = models.Idea.objects.create(
            title="Test Idea",             
            solution="Test solution"
        )        
        self.assertEqual(str(post), post.title)
        