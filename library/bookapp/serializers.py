from rest_framework import serializers
from .models import Book, Student, BorrowedBook, Librarian

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'borrowed_books']

class BorrowedBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowedBook
        fields = '__all__'

class LibrarianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Librarian
        fields = '__all__'
