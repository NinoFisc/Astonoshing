from django.shortcuts import render

from django.http import HttpResponse
from django.template import context, loader


from .models import Topic

# Create your views here.


def index(request):
    latest_topic_list = Topic.objects.all().order_by("-created_at")[:5]
    template = loader.get_template("polls/index.html")
    context = {"latest_topic_list":latest_topic_list}
    

    return HttpResponse(render(request,"polls/index.html", context))

def topic(request, topic_name):
    template = loader.get_template("polls/topic.html")
    context = {"topic_name": topic_name}

    return HttpResponse(template.render(context,template)) #HttpResponse(render(request, f"polls/topic.html"), context)
