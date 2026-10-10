from django.shortcuts import get_object_or_404, render
from .models import Book


def book_list(request):
    books = Book.objects.order_by("title")
    q = request.GET.get("q", "").strip()          # /?q=python
    if q:
        books = books.filter(title__icontains=q) | books.filter(author__icontains=q)
    return render(request, "library/1.html", {"books": books.distinct(), "q": q})


def book_detail(request, id):
    book = get_object_or_404(Book, id=id)        # shows a 404 page if id doesn't exist
    return render(request, "library/2.html", {"book": book})
