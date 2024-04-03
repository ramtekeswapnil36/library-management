from django.contrib import admin
from .models import Book, Student, BorrowedBook, Librarian

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'copies_available')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(BorrowedBook)
class BorrowedBookAdmin(admin.ModelAdmin):
    list_display = ('student', 'book', 'borrowed_date', 'due_date', 'renewed')

@admin.register(Librarian)
class LibrarianAdmin(admin.ModelAdmin):
    list_display = ('name',)

