
"""
Unit tests for Book API endpoints.

Tests Included:
- CRUD operations
- Filtering, searching, ordering
- Authentication and permission checks
"""

from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Author, Book


class BookAPITest(APITestCase):

    def setUp(self):
        """
        Create test user, author, and book objects.
        """
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123"
        )

        self.author = Author.objects.create(name="Test Author")

        self.book = Book.objects.create(
            title="Test Book",
            publication_year=2020,
            author=self.author
        )

        self.list_url = reverse("book-list")
        self.detail_url = reverse("book-detail", args=[self.book.id])
        self.create_url = reverse("book-create")
        self.update_url = reverse("book-update", args=[self.book.id])
        self.delete_url = reverse("book-delete", args=[self.book.id])

    # -------------------------------
    # TEST CREATE BOOK
    # -------------------------------
    def test_create_book_authenticated(self):
        self.client.login(username="testuser", password="testpass123")

        data = {
            "title": "New Book",
            "publication_year": 2021,
            "author": self.author.id
        }

        response = self.client.post(self.create_url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    # -------------------------------
    # TEST CREATE BOOK UNAUTHENTICATED
    # -------------------------------
    def test_create_book_unauthenticated(self):
        data = {
            "title": "Blocked Book",
            "publication_year": 2021,
            "author": self.author.id
        }

        response = self.client.post(self.create_url, data)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # -------------------------------
    # TEST GET BOOK LIST
    # -------------------------------
    def test_get_book_list(self):
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # -------------------------------
    # TEST GET SINGLE BOOK
    # -------------------------------
    def test_get_single_book(self):
        response = self.client.get(self.detail_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.book.title)

    # -------------------------------
    # TEST UPDATE BOOK
    # -------------------------------
    def test_update_book_authenticated(self):
        self.client.login(username="testuser", password="testpass123")

        data = {
            "title": "Updated Title",
            "publication_year": 2022,
            "author": self.author.id
        }

        response = self.client.put(self.update_url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # -------------------------------
    # TEST DELETE BOOK
    # -------------------------------
    def test_delete_book_authenticated(self):
        self.client.login(username="testuser", password="testpass123")

        response = self.client.delete(self.delete_url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # -------------------------------
    # TEST FILTERING
    # -------------------------------
    def test_filter_books(self):
        response = self.client.get(self.list_url + "?publication_year=2020")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # -------------------------------
    # TEST SEARCH
    # -------------------------------
    def test_search_books(self):
        response = self.client.get(self.list_url + "?search=Test")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # -------------------------------
    # TEST ORDERING
    # -------------------------------
    def test_order_books(self):
        response = self.client.get(self.list_url + "?ordering=title")

        self.assertEqual(response.status_code, status.HTTP_200_OK)