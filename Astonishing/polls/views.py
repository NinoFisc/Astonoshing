from django.shortcuts import render

from django.http import Http404, HttpResponse
from django.template import context, loader


from .models import Topic,Question,Customer

# Create your views here.


def index(request):
    latest_topic_list = Topic.objects.all().order_by("-created_at")[:5]
    context = {"latest_topic_list":latest_topic_list}
    
    return render(request, "polls/index.html", context)

def topic(request, topic_name):
    try:
        topic = Topic.objects.get(name=topic_name)
        questions = Question.objects.filter(topic=topic)

    except:
        raise Http404("Topic does not exist.")
        
    template = loader.get_template("polls/topic.html")
    context = {"topic_name": topic_name, "topic": topic,'questions':questions}

    return HttpResponse(template.render(context,template)) #HttpResponse(render(request, f"polls/topic.html"), context)
