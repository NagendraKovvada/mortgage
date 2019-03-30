from django.db import models
import uuid

# Create your models here.

class Client(models.Model):
	uuid = models.UUIDField(default=uuid.uuid4, editable=False)
	name = models.CharField(max_length=250)
	def __str__(self):
		return "{0}".format(self.name)

class Loans(models.Model):
	uuid = models.UUIDField(default=uuid.uuid4, editable=False)
	type = models.CharField(max_length=100,blank=True, null=True)
	def __str__(self):
		return "{0}".format(self.type)

class Loan_Details(models.Model):	
	uuid = models.UUIDField(default=uuid.uuid4, editable=False)
	loan_timestamp = models.DateTimeField(blank=True, null=True,auto_now_add=True)
	client = models.ForeignKey('Client',
                                 related_name='client_loan',
                                 blank=True,
                                 null=True,
                                 on_delete=models.DO_NOTHING)	
	Loan_type = models.ForeignKey('Loans',
                                 related_name='loan_type',
                                 blank=True,
                                 null=True,
                                 on_delete=models.DO_NOTHING)
	amount = models.DecimalField(decimal_places=1, max_digits=4, default=0)
	title = models.CharField(max_length=100,blank=True, null=True)
	description = models.CharField(max_length=100,blank=True, null=True)
	status = models.BooleanField(default=False)

	def __str__(self):
		return "{0} at {1} ".format(self.client,self.title)

