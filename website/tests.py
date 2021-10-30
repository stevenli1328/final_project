from django.test import TestCase

class HomepageViewTest(TestCase):

    def test_call_view_deny_anonymous(self):
        response = self.client.get('', follow=True)
        self.assertRedirects(response, '/profile/login/?next=/')
        response = self.client.post('', follow=True)
        self.assertRedirects(response, '/profile/login/?next=/')
