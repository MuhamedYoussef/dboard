import os
from base64 import b64decode
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views import View
from .models import PageView


class Script(View):

    def get(self, request):
        script_path = os.path.join(settings.BASE_DIR, 'dboard', 'static', 'js', 'script.js')
        with open(script_path, 'r') as script:
            content = script.read().replace('DOMAIN', 'http://localhost:8000')
            return HttpResponse(content=content, content_type='application/javascript')
        return JsonResponse({'err': 'Something went wrong!'}, safe=False)


class Analyse(View):

    def get(self, request):
        pageview = PageView.create_from_request(request)
        print(pageview)
        gif = b64decode('R0lGODlhAQABAIAAANvf7wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==')
        return HttpResponse(content=gif, content_type='image/gif')
