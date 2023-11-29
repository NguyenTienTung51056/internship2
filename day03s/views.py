# myapp/views.py
from django.shortcuts import render
from django.db.models import Count
from .models import Author, Book
from datetime import date

def book_list(request):
    # Lấy danh sách tất cả sách xuất bản sau năm 2020
    books_published_after_2020 = Book.objects.filter(published_date__gt=date(2020, 1, 1))

    # Lấy danh sách tất cả tác giả và số lượng sách của mỗi tác giả
    authors_with_book_count = Author.objects.annotate(book_count=Count('book'))

    # Lấy danh sách tất cả sách mà tác giả có tên là 'John Doe' đang tham gia vào
    books_by_john_doe = Book.objects.filter(authors__name='John Doe')

    return render(request, 'day03s/book_list.html', {
        'books_published_after_2020': books_published_after_2020,
        'authors_with_book_count': authors_with_book_count,
        'books_by_john_doe': books_by_john_doe,
    })
