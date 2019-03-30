from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import * 
from weasyprint import HTML,CSS
from django.template.loader import render_to_string
from django.core.files.storage import FileSystemStorage
from django.conf import settings

def html_to_pdf_view(request,id=None):
	# import pdb;pdb.set_trace()
	query = Loan_Details.objects.all()
	html_string = render_to_string('loan.html', {'form': query})
	# stylesheets=[CSS(settings.STATIC_ROOT +  'css/main.css')]CSS(settings.STATIC_ROOT +  'css/main.css')]
	html = HTML(string=html_string, base_url=request.build_absolute_uri())
	html.write_pdf(target='mortgage.pdf',stylesheets=[CSS(settings.STATIC_ROOT +  '/style.css')]);
	fs = FileSystemStorage()
	with fs.open('mortgage.pdf') as pdf:
		response = HttpResponse(pdf, content_type='application/pdf')
		response['Content-Disposition'] = 'inline; filename="mortgage.pdf"'
		return response

	return response