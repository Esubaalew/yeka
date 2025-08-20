import random
import shutil
from django.core.management.base import BaseCommand
from django.conf import settings
from portal.models import Author, Department, Research
from django.core.files import File
import os

class Command(BaseCommand):
    help = 'Populate the database with demo data for all models.'

    def handle(self, *args, **options):
        # Clear existing data
        Research.objects.all().delete()
        Author.objects.all().delete()
        Department.objects.all().delete()

        # Departments
        departments = [
            Department.objects.create(name='Computer Science'),
            Department.objects.create(name='Physics'),
            Department.objects.create(name='Mathematics'),
        ]

        # Authors
        authors = []
        for i in range(1, 9):
            author = Author.objects.create(
                first_name=f'Author{i}',
                last_name=f'Surname{i}',
                email=f'author{i}@example.com'
            )
            authors.append(author)

        # Use a sample file from media/research_files/ or create a dummy file
        sample_file_path = os.path.join(settings.MEDIA_ROOT, 'research_files', 'Enimar_code_learning__Hub1.pdf')
        if not os.path.exists(sample_file_path):
            # Create a dummy PDF if not present
            os.makedirs(os.path.dirname(sample_file_path), exist_ok=True)
            with open(sample_file_path, 'wb') as f:
                f.write(b'%PDF-1.4\n%Dummy PDF file for demo purposes')

        # Research
        for i in range(1, 11):
            research = Research.objects.create(
                title=f'Research Project {i}',
                summary=f'This is a summary of research project {i}.',
                department=random.choice(departments),
            )
            # Assign 1-3 random authors
            research.authors.set(random.sample(authors, random.randint(1, 3)))
            # Attach the sample file
            with open(sample_file_path, 'rb') as f:
                research.file.save(f'research_{i}.pdf', File(f), save=True)

        self.stdout.write(self.style.SUCCESS('Demo data populated for Authors, Departments, and Research.'))

