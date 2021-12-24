from django.db import connections, models
from django import forms
from django.db.models.fields import DateField, TextField
from django.forms.fields import ImageField, NullBooleanField
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
# model for drop down menu in add counsel form
class Borough(models.Model):
    OPTIONS = (
		('bronx', 'Bronx'),
		('brooklyn', 'Brooklyn'),
		('manhattan', 'Manhattan'),
        ('queens', 'Queens'),
		('staten island', 'Staten Island'),
	)

    def __init__(self, *args, Borough, **kwargs):
        self.borough = Borough
        return super().__init__(*args, **kwargs)
    
    borough = forms.ChoiceField(required=True, choices=OPTIONS)

# model for drop down menu in add counsel form 
class Status(models.Model):
    OPTIONS = (
		('legal aid / public defender', 'Legal Aid / Public Defender'),
		('private attorney', 'Private Attorney'),
	)

    def __init__(self, *args, Status, **kwargs):
        self.status = Status
        return super().__init__(*args, **kwargs)
    
    status = forms.ChoiceField(required=True, choices=OPTIONS)

# model for post
class Post(models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField(blank=True)
	User = models.CharField(max_length= 15)

	created = models.DateTimeField(default=timezone.now)
	updated = models.DateTimeField(default=timezone.now)
	visits = models.PositiveIntegerField(default=0)

	def __str__(self):
		return self.title

# model for comment section 
class Comment(models.Model):
	key = models.CharField(max_length= 15)
	post = models.ForeignKey(
		Post, on_delete=models.CASCADE, related_name='review')
	User = models.CharField(max_length= 15)
	body = models.TextField(blank=True)
	is_active = models.BooleanField(default=True)
	dateNtime = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.post.title

# model for counsel
class Counsel(models.Model):
    fName = models.CharField(max_length= 15)
    lName = models.CharField(max_length= 15)
    firmN = models.CharField(max_length= 100)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, default='Legal Aid / Public Defender')
    phoneN = models.IntegerField()
    Address = models.CharField(max_length= 15)
    Address2 = models.CharField(max_length= 15)
    zip_code = models.IntegerField()
    borough = models.ForeignKey(Borough, choices=Borough.OPTIONS, on_delete=models.CASCADE, default='draft')
    state = models.CharField(max_length= 15) 
    comment = models.ForeignKey(Comment, blank=True, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.name

# model for viewing counseling information
class ViewCounsel(models.Model):
    pass

# model for viewing counsel profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg')
    Comment = models.ForeignKey(Comment, on_delete=models.CASCADE,blank=True, null=True)


    def __str__(self):
        return f'{self.user.username}Profile'