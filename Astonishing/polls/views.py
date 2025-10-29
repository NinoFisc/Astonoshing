
from django.shortcuts import redirect, render

from django.http import Http404, HttpResponse
from django.template import context, loader



from .models import Topic,Question,Customer

from .forms import QuestionForm, TopicForm

# Create your views here.


def index(request):

    try:
        latest_topic_list = Topic.objects.all().order_by("-created_at")[:5]
        customer = Customer.objects.all().order_by("created_at")[0]
        context = {"latest_topic_list":latest_topic_list}

        if request.method == 'POST':
            form = TopicForm(request.POST)

            if form.is_valid():
                topic = form.save(commit=False)
                topic.customer = customer
                topic.save()


        if request.method == 'GET':
            form = TopicForm()

    except Exception as e:
        raise Http404(f'Error: {e}')

    context = {
        "latest_topic_list":latest_topic_list,
        'form': form
        }
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







        
