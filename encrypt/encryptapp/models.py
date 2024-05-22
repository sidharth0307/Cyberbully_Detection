from django.db import models

# Create your models here.
class police_station(models.Model):
	name=models.CharField(max_length=50)
	phone_number=models.CharField(max_length=15)
	email=models.EmailField(max_length=50)
	address=models.TextField(max_length=200)
	image=models.ImageField(upload_to="data",blank=True)
	

	def __str__(self):
		return self.name

class FAQ(models.Model):
	question=models.TextField(max_length=200)
	answer=models.TextField(max_length=1000)

	def __str__(self):
		return self.question


class Laws(models.Model):
	sections=models.TextField(max_length=30)
	offence=models.TextField(max_length=300)
	penalty=models.TextField(max_length=200)


	def __str__(self):
		return ("sectin"+" "+self.sections)

class cybersecurity_laws(models.Model):
	name=models.TextField(max_length=100)
	description=models.TextField(max_length=1500)

	def __str__(self):
		return self.name


class Terms(models.Model):
	title=models.TextField(max_length=100)
	description=models.TextField(max_length=400)
	image=models.ImageField(upload_to="data",blank=True)

	def __str__(self):
		return self.title

class userregister(models.Model):
	name=models.CharField(max_length=50)
	email=models.EmailField(max_length=50)
	first=models.CharField(max_length=50, blank=True, null=True)
	last=models.CharField(max_length=50, blank=True, null=True)
	contactno=models.CharField(max_length=15, blank=True,null=True)
	password=models.TextField(max_length=40)
	address=models.CharField(max_length=1000, blank=True, null=True)
	address2=models.CharField(max_length=1000, blank=True, null=True)
	gender=models.CharField(max_length=100, blank=True, null=True)
	city=models.CharField(max_length=100, blank=True, null=True)
	state=models.CharField(max_length=100, blank=True, null=True)
	pin=models.CharField(max_length=100, blank=True, null=True)
	dob=models.CharField(max_length=100, blank=True, null=True)
	image=models.ImageField(upload_to="data",blank=True, null=True)

	def __str__(self):
		return self.name

class contact_us(models.Model):
	name=models.CharField(max_length=50)
	email=models.EmailField(max_length=50)
	company_name=models.TextField(max_length=100)
	message=models.TextField(max_length=1000)

class review(models.Model):
	username=models.CharField(max_length=50)
	title=models.TextField(max_length=200)
	message=models.TextField(max_length=1000)

	def __str__(self):
		return self.username


class help_support(models.Model):
	username=models.CharField(max_length=50)
	title=models.TextField(max_length=200)
	message=models.TextField(max_length=1000)

	def __str__(self):
		return self.username

