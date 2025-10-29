from django.shortcuts import redirect, render

from django.http import Http404, HttpResponse
from django.template import context, loader



from .models import Topic,Question,Customer

from .forms import QuestionForm

# Create your views here.


def index(request):
    latest_topic_list = Topic.objects.all().order_by("-created_at")[:5]
    context = {"latest_topic_list":latest_topic_list}
    
    return render(request,
    "polls/index.html",
    context)

def topic(request, topic_name):
    try:

        topic = Topic.objects.get(name=topic_name)
        questions = Question.objects.filter(topic=topic)

        if request.method == 'POST':
            form = QuestionForm(request.POST)

            if form.is_valid():

                question = form.save(commit=False)
                question.topic = topic
                question.save()
        


        if request.method == 'GET':
            form = QuestionForm()

    except:
        raise Http404("Topic does not exist.")
        
    context = {
        "topic_name": topic_name,
        "topic": topic,
        'questions':questions,
        "form":form
        }

    return render(
    request,
    "polls/topic.html",
    context
      ) #HttpResponse(render(request, f"polls/topic.html"), context)







        
