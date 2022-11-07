from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successfull(self):
        email = 'test@example.com'
        pseudo = 'testpseudo'
        password = 'testpass123'
        user = get_user_model().objects.create_user(email=email, pseudo=pseudo, password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.COM', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com']
        ]

        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, "sample123")
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raise_error(self):
        """
        The test_new_user_without_email_raise_error function tests that a ValueError is raised when the user does not provide an email address.
        It creates a new user without an email address and then checks to see if the value error was raised.

        :param self: Access variables that belongs to the test case class
        :return: The following:
        :doc-author: Trelent
        """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', "sample123")

    def test_create_superuser(self):
        user = get_user_model().objects.create_superuser(
            'test1@example.com',
            'test1123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
