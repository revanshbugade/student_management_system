from django.db import models
courses=(('Cloud Computing','Cloud Computing'),
         ('Data Analytics','Data Analytics'),
         ('Python Programing','Python Programing'),
         ('Web Development','Web Development'),
         ('UI/UX Development','UI/UX Development'))
timing=(('Morning','Morning'),
        ('Afternoon','Afternoon'),('Evening','Evening'))

class StudentsModel(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.IntegerField()
    course=models.CharField(max_length=200,choices=courses)
    course_timing=models.CharField(max_length=200,choices=timing)
    def __str__(self):
        return self.first_name
