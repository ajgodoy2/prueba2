from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.csrf import ensure_csrf_cookie

from books.forms import ReviewForm
from books.models import Book, Author, ReviewWriter, Review


def browse(request):
    entities = (('book', 'books'), ('author', 'authors'))
    others = (['author'], ['book'])
    entity = entities[0 if request.GET['by'] == 'book' else 1]
    other = others[0 if request.GET['by'] == 'book' else 1]

    if 'q' in request.GET:
        # User wants to search
        if request.GET['by'] == 'book':
            elems = Book.objects.filter(title__icontains=request.GET['q'])
        else:
            elems = Author.objects.filter(name__icontains=request.GET['q'])
    else:
        # User wants all
        if request.GET['by'] == 'book':
            elems = Book.objects.all()
        else:
            elems = Author.objects.all()

    return render(request, 'list_and_search.html',
                  {'entity': entity,
                   'others': other,
                   'elems': elems})


def book(request, book_id):
    book = Book.objects.get(id=int(book_id))
    return render(request, 'details_book.html', {'book': book})


def author(request, author_id):
    author = Author.objects.get(id=int(author_id))
    return render(request, 'details_author.html', {'author': author})


@login_required
def add_read(request, book_id):
    book = Book.objects.get(id=book_id)
    if book not in request.user.reviewwriter.read_books.all():
        request.user.reviewwriter.read_books.add(book)
    return redirect(reverse('book', kwargs={'book_id': book_id}))


@login_required
def delete_read(request, book_id):
    book = Book.objects.get(id=book_id)
    request.user.reviewwriter.read_books.remove(book)
    return redirect(reverse('account'))


@login_required
def add_review(request, book_id):
    book = Book.objects.get(id=book_id)
    if Review.objects.filter(writer=request.user.reviewwriter, book=book):
        # Avoid duplicate reviews here, one per author and book
        return redirect(reverse('book', kwargs={'book_id': book_id}))
    if request.method == 'POST':
        # Data has been submitted
        form = ReviewForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Review.objects.create(rating=cd['rating'],
                                  opinion=cd['opinion'],
                                  writer=request.user.reviewwriter,
                                  book=book)
            return redirect(reverse('book', kwargs={'book_id': book_id}))
    else:
        # First time, don't validate
        form = ReviewForm()
    return render(request, 'add_review.html', {'form': form})


def delete_review(request, book_id):
    book = Book.objects.get(id=book_id)
    if Review.objects.filter(writer=request.user.reviewwriter, book=book):
        # User has reviewed, otherwise skip
        Review.objects.filter(writer=request.user.reviewwriter,
                              book=book).delete()
    return redirect(reverse('book', kwargs={'book_id': book_id}))


def new_book(request):
    return render(request, 'new_book.html')
