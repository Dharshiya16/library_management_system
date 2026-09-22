from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm


def book_list(request):

    search = request.GET.get('search', '')

    books = Book.objects.filter(
        title__icontains=search
    )

    return render(
        request,
        'books/book_list.html',
        {
            'books': books,
            'search': search
        }
    )


def book_add(request):

    if request.method == 'POST':
        form = BookForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('book_list')

    else:
        form = BookForm()

    return render(
        request,
        'books/book_form.html',
        {'form': form}
    )
def book_delete(request, id):

    book = Book.objects.get(id=id)
    book.delete()

    return redirect('book_list')
def book_edit(request, id):

    book = Book.objects.get(id=id)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)

        if form.is_valid():
            form.save()
            return redirect('book_list')

    else:
        form = BookForm(instance=book)

    return render(
        request,
        'books/book_form.html',
        {'form': form}
    )