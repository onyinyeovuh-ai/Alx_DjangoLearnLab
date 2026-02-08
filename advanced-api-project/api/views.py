"""
This module defines CRUD API views for the Book model.

Generic Views Used:
- ListAPIView: Retrieves all books
- RetrieveAPIView: Retrieves a book by ID
- CreateAPIView: Creates a new book (Authenticated users only)
- UpdateAPIView: Updates an existing book (Authenticated users only)
- DestroyAPIView: Deletes a book (Authenticated users only)

Permissions:
- Read operations are public
- Write operations require authentication
"""

from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# -------------------------------
# LIST VIEW
# Returns all books
# Allows read-only access for everyone
# -------------------------------
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# -------------------------------
# DETAIL VIEW
# Returns one book by ID
# Allows read-only access for everyone
# -------------------------------
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# -------------------------------
# CREATE VIEW
# Allows authenticated users to create books
# -------------------------------
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# -------------------------------
# UPDATE VIEW
# Allows authenticated users to update books
# -------------------------------
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# -------------------------------
# DELETE VIEW
# Allows authenticated users to delete books
# -------------------------------
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]