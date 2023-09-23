from django.db import models

# Create your models here.
class PersonalDetails(models.Model):
    name=models.CharField(max_length=100, null=True, blank=True)
    age=models.CharField(max_length=10, null=True, blank=True)
    picture=models.ImageField()
    address=models.CharField(max_length=100, null=True, blank=True)
    phone_number=models.CharField(max_length=100, null=True, blank=True)
    email=models.EmailField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    
class AboutMyself(models.Model):
    years_of_experience=models.CharField(max_length=10, null=True, blank=True )
    short_note=models.TextField(null=True, blank=True)
    title=models.CharField(max_length=300, null=True, blank=True)
    
    if years_of_experience is not None:
        def __str__(self):
            return self.years_of_experience + " " + "years"
    else:
        pass
        

class Skills(models.Model):
    skill_name=models.CharField(max_length=50, null=True, blank=True)
    skill_percent=models.IntegerField(default=0)
     
    if skill_name is not None:
        def __str__(self):
            return self.skill_name
    else:
        pass
class SchoolExperience(models.Model):
    name=models.CharField(max_length=100, null=True, blank=True)
    start_date=models.CharField(max_length=10, null=True, blank=True)
    end_date=models.CharField(max_length=10, null=True, blank=True)
    org_name=models.CharField(max_length=100, null=True, blank=True)
    is_school=models.BooleanField(default=True)
    
     
    if name is not None:
        def __str__(self):
            return self.org_name
    else:
        pass
    
class Services(models.Model):
    name=models.CharField(max_length=100, null=True, blank=True)
    price=models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    short_note=models.TextField()
    
     
    if name is not None:
        def __str__(self):
            return self.name
    else:
        pass
    
class Projects(models.Model):
    name=models.CharField(max_length=100, null=True, blank=True)
    image_file=models.ImageField()
    date_created=models.DateTimeField(auto_now_add=True)
    is_graphic=models.BooleanField(default=True)
    link=models.URLField(null=True, blank=True)
    
       
    if name is not None:
        def __str__(self):
            return self.name
    else:
        pass
    
class MessageReport(models.Model):
    name=models.CharField(max_length=100, null=True, blank=True)
    email=models.EmailField(null=True, blank=True)
    subject=models.CharField(max_length=200, null=True, blank=True)
    msg_body=models.TextField(null=True, blank=True)
    
    if name is not None:
        def __str__(self):
            return self.name
    else:
        pass
    
    