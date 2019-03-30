from django.contrib import admin
from .models import *

admin.site.register(Client)
admin.site.register(Loans)
admin.site.register(Loan_Details)