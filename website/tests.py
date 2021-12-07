from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class HomepageViewTest(TestCase):
    def test_call_view_deny_anonymous(self):
        response = self.client.get('', follow=True)
        self.assertRedirects(response, '/profile/login/?next=/')
        response = self.client.post('', follow=True)
        self.assertRedirects(response, '/profile/login/?next=/')

class SigninTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='test', email='test@example.com')
        self.user.set_password('12test12')
        self.user.save()

    def test_correct(self):
        user = authenticate(username='test', password='12test12')
        self.assertTrue(user is not None and user.is_authenticated)

    def test_wrong_username(self):
        user = authenticate(username='wrong', password='12test12')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_pssword(self):
        user = authenticate(username='test', password='wrong')
        self.assertFalse(user is not None and user.is_authenticated)
