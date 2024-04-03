from django.db import models
from django.utils import timezone

class Book(models.Model):
    title = models.CharField(max_length=100)
    copies_available = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title

class Student(models.Model):
    name = models.CharField(max_length=100)
    borrowed_books = models.ManyToManyField(Book, through='BorrowedBook')
    
    
    
    def __str__(self):
        return self.name

class BorrowedBook(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowed_date = models.DateField(default=timezone.now)
    due_date = models.DateField()
    renewed = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.pk is None:  # Check if this is a new instance
            self.book.copies_available -= 1  # Decrement available copies when borrowing
            self.book.save()
        super().save(*args, **kwargs)

    def renew(self):
        if not self.renewed:
            self.due_date += timezone.timedelta(days=30)
            self.renewed = True
            self.save()

    def delete(self, *args, **kwargs):
        self.book.copies_available += 1  # Increment available copies when returning
        self.book.save()
        super().delete(*args, **kwargs)

    def __str__(self):
        return f"{self.student.name} - {self.book.title}"

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    
    def mark_borrowed(self, student, book):
        if book.copies_available > 0:
            BorrowedBook.objects.create(student=student, book=book, due_date=timezone.now() + timezone.timedelta(days=30))
            return True
        else:
            return False

    def mark_returned(self, borrowed_book):
        borrowed_book.delete()

    def get_borrowed_books(self, student):
        return BorrowedBook.objects.filter(student=student)

    def __str__(self):
        return self.name

