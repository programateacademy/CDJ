from django.test import TestCase
from .models import Post
from home.models import Consejos
from django.contrib.auth.models import User

# Create your tests here.

class PostModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.consejo = Consejos.objects.create(title='testtitle', text='testtext')
        self.post = Post.objects.create(title='testtitle', text='testtext', user=self.user, consejo=self.consejo)

    def test_post_title(self):
        post = Post.objects.get(id=1)
        self.assertEqual(post.title, 'testtitle')

    def test_post_text(self):
        post = Post.objects.get(id=1)
        self.assertEqual(post.text, 'testtext')

    def test_post_user(self):
        post = Post.objects.get(id=1)
        self.assertEqual(post.user, self.user)

    def test_post_consejo(self):
        post = Post.objects.get(id=1)
        self.assertEqual(post.consejo, self.consejo)
