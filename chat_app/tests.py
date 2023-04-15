from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .views import chat

class ChatAppTests(TestCase):

    def test_chat_view_with_no_username(self):
        """
        Test that the chat view redirects to the entry page if no username is provided.
        """
        response = self.client.get(reverse('chat'), {'username': ''})
        self.assertTemplateUsed(response, 'chat_app/entry.html')

    def test_chat_view_with_username(self):
        """
        Test that the chat view renders the chat template with the provided username.
        """
        response = self.client.get(reverse('chat'), {'username': 'test_user'})
        self.assertTemplateUsed(response, 'chat_app/chat.html')
        self.assertEqual(response.context['username'], 'test_user')

