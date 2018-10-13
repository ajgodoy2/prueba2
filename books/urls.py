from django.conf.urls import url
import books.views

urlpatterns = [
    url(r'^browse/$', books.views.browse, name='browse'),
    url(r'^book/(?P<book_id>\d+)/$', books.views.book, name='book'),
    url(r'^author/(?P<author_id>\d+)/$', books.views.author, name='author'),
    url(r'^book/(?P<book_id>\d+)/add_read/$', books.views.add_read, name='add_read'),
    url(r'^book/(?P<book_id>\d+)/delete_read/$', books.views.delete_read, name='delete_read'),
    url(r'^book/(?P<book_id>\d+)/add_review/$', books.views.add_review, name='add_review'),
    url(r'^book/(?P<book_id>\d+)/delete_review/$', books.views.delete_review, name='delete_review'),
    url(r'^new_book/$', books.views.new_book)
]
