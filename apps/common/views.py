from django.views.generic import TemplateView
from django.shortcuts import render_to_response


class HomePageView(TemplateView):
    template_name = "common/main.html"


def handler404(request, exception, template_name="common/404.html"):
    response = render_to_response(template_name)
    response.status_code = 404
    return response


def handler500(request, exception=None, template_name="common/500.html"):
    response = render_to_response(template_name)
    response.status_code = 500
    return response

# def error(request):
#     pass

