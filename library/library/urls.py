
from django.contrib import admin
from django.urls import path
# from bookapp import views
from bookapp.views import info, BookListCreateAPIView, StudentListCreateAPIView, BorrowedBookListCreateAPIView, LibrarianListCreateAPIView


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('book/',views.available_books),
    # path('borrow/<int:book_id>/',views.borrow_book),
    # path('borrowed-books/', views.borrowed_books)
    path('',info),
    path('books/', BookListCreateAPIView.as_view(), name='book-list-create'),
    path('students/', StudentListCreateAPIView.as_view(), name='student-list-create'),
    path('borrowed-books/', BorrowedBookListCreateAPIView.as_view(), name='borrowed-book-list-create'),
    path('librarians/', LibrarianListCreateAPIView.as_view(), name='librarian-list-create'),


]
