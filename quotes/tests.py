from django.test import TestCase
from django.contrib.auth.models import User
from .models import Author, Quote, Tag

class AuthorModelTest(TestCase):
    def test_author_creation(self):
        author = Author.objects.create(name="Test Author", born="2000", bio="Bio")
        self.assertEqual(str(author), "Test Author")

class QuoteModelTest(TestCase):
    def test_quote_creation(self):
        author = Author.objects.create(name="Author")
        quote = Quote.objects.create(text="Some text", author=author)
        self.assertEqual(str(quote), "Some text...")

class TagModelTest(TestCase):
    def test_tag_creation(self):
        tag = Tag.objects.create(name="inspiration")
        self.assertEqual(str(tag), "inspiration")
