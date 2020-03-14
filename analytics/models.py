from django.db import models
from .utils import get_client_ip

class PageView(models.Model):
    domain = models.CharField(max_length=200)
    ip_addr = models.CharField(max_length=50)
    lang = models.CharField(max_length=50)
    url = models.TextField()
    title = models.TextField()
    referrer = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


    @classmethod
    def create_from_request(cls, request):
        headers = request.headers
        data= request.GET
        ip = get_client_ip(request)

        return cls.objects.create(
            domain=headers['Host'],
            ip_addr=ip,
            lang=headers['Accept-Language'],
            url=data['url'],
            title=data['title'],
            referrer=data['ref']
        )