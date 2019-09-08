from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render

# Create your views here.

def gitupdate(request):
	log = []
	try:
		import git
		from django.core.management import call_command
		import os
		import time

		g = git.cmd.Git("C:\\Users\\Sayaka\\Documents\\GitHub\\butler")
		g.fetch()
		g.pull()
		time.sleep(10)
		try:
			call_command('makemigrations')
			log.append("makemigrations Complete")
			call_command('migrate')
			log.append("migrate Complete")
			call_command('collectstatic', verbosity=0, interactive=False)
			log.append("collectstatic Complete")
		except Exception as e:
			log.append(e)
		

		return JsonResponse({"Success":"", "log":log})
	except Exception as e:
		import sys, os
		exc_type, exc_obj, exc_tb = sys.exc_info()
		other = sys.exc_info()[0].__name__
		fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
		errorType = str(exc_type)
		errob = {"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log}
		return JsonResponse(errob)