from django.core.exceptions import ValidationError
from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# Define the Department model
class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Define the Research model
class Research(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField()
    authors = models.ManyToManyField(Author, related_name='researches', db_index=True)  # Many-to-Many relationship
    department = models.ForeignKey(Department, on_delete=models.CASCADE,
                                   related_name='researches', db_index=True)  # Many-to-One relationship
    file = models.FileField(upload_to='research_files/', blank=True, null=True)  # File upload (PDF/Word)

    def __str__(self):
        return self.title

    # Ensuring the file is either a PDF or Word document
    def clean(self):
        if self.file:
            file_ext = self.file.name.split('.')[-1].lower()
            if file_ext not in ['pdf', 'doc', 'docx']:
                raise ValidationError('File must be in PDF, DOC, or DOCX format.')
