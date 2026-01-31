from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import
from .forms import ExampleForm

# Create your views here.
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        # Using Django ORM instead of raw SQL to prevent SQL injection
        title = request.POST.get('title')
        author = request.POST.get('author')

        Book.objects.create(
            title=title,
            author=author
        )
        return redirect('book_list')

    return render(request, 'bookshelf/create_book.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        # Using Django ORM instead of raw SQL to prevent SQL injection
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.save()
        return redirect('book_list')

    return render(request, 'bookshelf/edit_book.html', {'book': book})

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('book_list')