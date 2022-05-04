from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager
import datetime
from webdev import settings

class User(AbstractBaseUser):

	email = models.EmailField(
		verbose_name='email',
		max_length=255,
		unique=True,
	)
	first_name = models.CharField(max_length=50,default='John')
	last_name = models.CharField(max_length=50,default='Doe')
	phone_number = models.CharField(max_length=12)


	is_active = models.BooleanField(default=True)
	staff = models.BooleanField(default=False) # a admin user; non super-user
	admin = models.BooleanField(default=False) # a superuser


	# notice the absence of a "Password field", that is built in.

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = [] # Email & Password are required by default.
	objects = UserManager()
	def __str__(self):
		full_name = self.first_name + ' ' + self.last_name 
		return full_name
		#return self.email
	def has_perm(self, perm, obj=None):
		# "Does the user have a specific permission?"
		# Simplest possible answer: Yes, always
		return True

	def has_module_perms(self, app_label):
		"Does the user have permissions to view the app `app_label`?"
		# Simplest possible answer: Yes, always
		return True

	@property
	def is_staff(self):
		"Is the user a member of staff?"
		return self.staff

	@property
	def is_admin(self):
		"Is the user a admin member?"
		return self.admin

class Role(models.Model):
	role_name = models.CharField(max_length=200,help_text="Enter Role")
	user = models.ForeignKey(User,on_delete=models.CASCADE)

class Education(models.Model):
	school_name = models.CharField(max_length=255,help_text="Enter your school name")
	major = models.CharField(max_length=255,help_text="Enter your major")

	DEGREE_CHOICES = (
	('bachelors','BACHELORS'),
	('masters', 'MASTERS'),
	('phd','PHD'),
	('mba','MBA'),
	('associate','ASSOCIATE'),
	)

	degree_type = models.CharField(max_length=10,choices=DEGREE_CHOICES)
	start_year = models.IntegerField(help_text="Enter Start Year")
	end_year = models.IntegerField(help_text="Enter End Year")
	def __str__(self):
		# """String for representing the MyModelName object (in Admin site etc.)."""
		return self.school_name  

	role = models.ForeignKey(Role,on_delete=models.CASCADE)      

class WorkExperience(models.Model):
	company_name = models.CharField(max_length=150,help_text="Enter company name")
	position_title = models.CharField(max_length=100,help_text="Enter your position")

	EXPERIENCE_CHOICES = (
	('internship','INTERNSHIP'),
	('part-time', 'PART-TIME'),
	('full-time','FULL-TIME'),
	)

	MONTH_CHOICES = (
		('january','JANUARY'),
		('february','FEBRUARY'),
		('march','MARCH'),
		('april','APRIL'),
		('may','MAY'),
		('june','JUNE'),
		('july','JULY'),
		('august','AUGUST'),
		('september','SEPTEMBER'),
		('october','OCTOBER'),
		('november','NOVEMBER'),
		('december','DECEMBER'),

		)

	experience = models.CharField(max_length=12,help_text="Select your experience",choices=EXPERIENCE_CHOICES)
	location = models.CharField(max_length=150,help_text="Enter your location")
	
	YEAR_CHOICES = []

	for x in range(1960,(datetime.datetime.now().year)):
		YEAR_CHOICES.append(
			(x,x)
			)

	start_year = models.IntegerField(help_text="Enter Start Year",choices=YEAR_CHOICES)
	end_year = models.IntegerField(help_text="Enter End Year",choices=YEAR_CHOICES)

	start_month = models.CharField(max_length=12,help_text="Enter Start Month",choices=MONTH_CHOICES)
	end_month = models.CharField(max_length=12,help_text="Enter End Month",choices=MONTH_CHOICES)
	description = models.CharField(max_length=1000)

	role = models.ForeignKey(Role,on_delete=models.CASCADE)

User = settings.AUTH_USER_MODEL

class Document(models.Model):
	cover_letter = models.FileField(upload_to= 'documents/cover_letter/',null=True)
	resume = models.FileField(upload_to= 'documents/resume/',null=True)
	role = models.OneToOneField(Role,on_delete=models.CASCADE,primary_key=True)

class URL(models.Model):
	linkedin = models.CharField(max_length=100, help_text="Enter URL") 
	github = models.CharField(max_length=100, help_text="Enter URL")
	portofolio = models.CharField(max_length=100, help_text="Enter URL")

	user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)

# class Skills