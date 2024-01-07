from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Author(AbstractUser):
    date = models.CharField(max_length=255)
    addres = models.CharField(max_length=255)
    zip_code = models.BigIntegerField()
    phone = models.CharField(max_length=255)
    desc = models.TextField()
    img = models.ImageField(upload_to='user')


    def __str__(self):
        return self.username
    


class Works(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='work')
    owner = models.ForeignKey(Author,on_delete=models.CASCADE,blank=True)


    def __str__(self):
        return self.name
    

class Education(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    from_date = models.CharField(max_length=255)
    to_date = models.CharField(max_length=255)
    author = models.ForeignKey(Author,on_delete=models.CASCADE,blank=True)


    def __str__(self):
        return self.title


class Experience(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    from_date = models.CharField(max_length=255)
    to_date = models.CharField(max_length=255)
    author = models.ForeignKey(Author,on_delete=models.CASCADE,blank=True)


    def __str__(self):
        return self.title


class Award(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    from_date = models.CharField(max_length=255)
    to_date = models.CharField(max_length=255)
    author = models.ForeignKey(Author,on_delete=models.CASCADE,blank=True)


    def __str__(self):
        return self.title
    

class Skill_one(models.Model):
    title = models.CharField(max_length=255)
    main_procent = models.IntegerField()
    week = models.IntegerField()
    month = models.IntegerField()
    author = models.ForeignKey(Author,on_delete=models.CASCADE,blank=True)


    def __str__(self):
        return self.title
    

class Skill_two(models.Model):
    title = models.CharField(max_length=255)
    main_procent = models.IntegerField()
    author = models.ForeignKey(Author,on_delete=models.CASCADE,blank=True)


    def __str__(self):
        return self.title
    

class Services(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    img = models.ImageField(upload_to='service')
    author = models.ForeignKey(Author,on_delete=models.CASCADE,blank=True)


    def __str__(self):
        return self.title




class Projects(models.Model):
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to='experience')
    author = models.ForeignKey(Author,on_delete=models.CASCADE,blank=True)


    def __str__(self):
        return self.title
    

class Nums(models.Model):
    awards = models.IntegerField()
    projects = models.IntegerField()
    customers = models.IntegerField()
    coffee = models.IntegerField()
    author = models.ForeignKey(Author,on_delete=models.CASCADE,blank=True)


    def __str__(self):
        return self.author.username



class Blog(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    content = models.TextField()
    img = models.ImageField(upload_to='blog')
    author = models.ForeignKey(Author,on_delete=models.CASCADE,blank=True)
    paragraph = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField('Caterories',related_name='caterories')
    

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    msg = models.TextField()
    author = models.ForeignKey(Author,on_delete=models.CASCADE,blank=True)


    def __str__(self):
        return self.author.username
    

class Caterories(models.Model):
    name = models.CharField(max_length=255)


    def __str__(self):
        return self.name
    

class Contact(models.Model):
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField()
    website = models.URLField()
    author = models.ForeignKey(Author,on_delete=models.CASCADE,blank=True)


    def __str__(self):
        return self.author.username

