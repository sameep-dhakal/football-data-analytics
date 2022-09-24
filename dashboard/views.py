# from django.http import JsonResponse
# from django.shortcuts import render
# from dashboard.models import *
# from django.core import serializers
# import pandas as pd

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'main.html')

def matches(request):
    return render(request, 'matches.html')

def blog(request):
    return render(request, 'blog.html')

def players(request):

    return render(request, 'players.html', mydict)     




   
# def players(request):

#     course_detail = {
#             "title": "Learning Python for Data Analysis and Visualization",
#             "descclass StudentCourseDetailView(View):ription": "Learn python and how to use it to analyze,visualize and present data. Includes tons of sample code and hours of video!",
#             "author": "John Doe",
#             "thumbnail": "data:image/png;base64,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",
#             "objectives": ["Have an intermediate skill level of Python programming.", "Use the Jupyter Notebook Environment.", "Use the numpy library to create and manipulate arrays.", "Use the pandas module with Python to create and structure data."],
#             "course_content": {
#                 "description": "15 sections • 110 lectures • 21h 5m total length",
#                 "chapters": [
#                     {"title": "Intro to Course Python",
#                         "length": "2 lectures • 25m "},
#                     {"title": "Intro to Pandas", "length": "3 lectures • 15m "}
#                 ]
#             }
#         }

#     context["qs"] = { "a":1, 'b':2}   
#     # context = {
#     #         "course": course_detail
#     #     }

#     return render(request, "players.html", context["qs"])
     
def contact(request):

    return render(request, 'contact.html')

def single_blog(request):
    return render(request, 'single.html')    

# def pivot_data(request):
#     dataset = Order.objects.all()
#     data = serializers.serialize('json', dataset)
#     return JsonResponse(data, safe=False)


from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Editors


# Creating views
class EditorChartView(TemplateView):
    template_name = 'players.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = Editors.objects.all()
        return context

