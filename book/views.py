from django.shortcuts import render, HttpResponse
from .models import Books
from django.contrib.auth.decorators import login_required


def dashboard(request):
    books = Books.objects.all()
    return render(request, 'book_index.html', {'books': books})


@login_required
def book_detail(request, pk):
    book = Books.objects.get(pk=pk)
    return render(request, 'book_detail.html', {'book': book})


@login_required
def addbook(request):
    books = Books.objects.all()
    if request.method == "POST":
        
        name = request.POST['name']
        author = request.POST['author']
        description = request.POST['description']
        rating = request.POST['rating']
        release_date = request.POST['release_date']
        cover_photo = request.FILES['cover_photo']
        book_file = request.FILES['book_file']
        book = Books.objects.create(
            name=name,
            author=author,
            description=description,
            rating=rating,
            release_date=release_date,
            cover_photo=cover_photo,
            book_file=book_file,
        )
        book.save()
    return render(request, "addbook.html", {'books': books})

