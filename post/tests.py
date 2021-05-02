from django.test import TestCase
from django.contrib.auth.models import User 
from .models import Post 

class PostTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create_user(username="test", password="test1234")
        test_user.save()
        post_user = Post.objects.create(author=test_user, title="primo post", text="ecco il mio post")
        post_user.save()

    def test_blog(self):
        oggetto = Post.objects.get(id=1)
        author = f'{oggetto.author}'
        title_1 = f'{oggetto.title}'
        text_1 = f'{oggetto.text}'
        self.assertEquals(author, "test")
        self.assertEquals(title_1, "primo post")
        self.assertEquals(text_1, "ecco il mio post")

