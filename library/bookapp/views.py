from django.shortcuts import render, redirect
# from .models import Book, Student, BorrowedBook, Librarian

# def available_books(request):
#     books = Book.objects.filter(copies_available__gt=0)
    
#     return render(request, 'available_books.html', {'books': books})

# def borrow_book(request, book_id):
#     book = Book.objects.get(id=book_id)
#     if request.method == 'POST':
#         student_name = request.POST.get('student_name')
#         student, created = Student.objects.get_or_create(name=student_name)
#         librarian = Librarian.objects.first()  # Assume there's only one librarian
#         if librarian.mark_borrowed(student, book):
#             return redirect('/borrowed_books/')
#     return render(request, 'borrow_book.html', {'book': book})

# def borrowed_books(request):
#     # Assuming there's a currently logged in student or librarian
#     user = request.user
#     if isinstance(user, Student):
#         borrowed_books = user.borrowed_books.all()
#     elif isinstance(user, Librarian):
#         borrowed_books = BorrowedBook.objects.all()
#     else:
#         borrowed_books = []
#     return render(request, 'borrowed_books.html', {'borrowed_books': borrowed_books})

# def return_book(request, borrowed_book_id):
#     borrowed_book = BorrowedBook.objects.get(id=borrowed_book_id)
#     if request.method == 'POST':
#         librarian = Librarian.objects.first()  # Assume there's only one librarian
#         librarian.mark_returned(borrowed_book)
#         return redirect('borrowed_books')
#     return render(request, 'return_book.html', {'borrowed_book': borrowed_book})

# def renew_book(request, borrowed_book_id):
#     borrowed_book = BorrowedBook.objects.get(id=borrowed_book_id)
#     if request.method == 'POST':
#         borrowed_book.renew()
#         return redirect('borrowed_books')
#     return render(request, 'renew_book.html', {'borrowed_book': borrowed_book})



from rest_framework import generics
from .models import Book, Student, BorrowedBook, Librarian
from .serializers import BookSerializer, StudentSerializer, BorrowedBookSerializer, LibrarianSerializer

class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class StudentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class BorrowedBookListCreateAPIView(generics.ListCreateAPIView):
    queryset = BorrowedBook.objects.all()
    serializer_class = BorrowedBookSerializer

class LibrarianListCreateAPIView(generics.ListCreateAPIView):
    queryset = Librarian.objects.all()
    serializer_class = LibrarianSerializer


def info(request):
    return render(request, 'index.html')
