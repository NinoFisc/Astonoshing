
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required


from django.http import Http404, HttpResponse
from django.template import context, loader



from .models import Topic,Question,Customer

from .forms import QuestionForm, TopicForm

# Create your views here.

@login_required
def index(request):

    try:
        latest_topic_list = Topic.objects.all().order_by("-created_at")[:5]
        customer = get_object_or_404(Customer,id=request.user.id)
        context = {"latest_topic_list":latest_topic_list}

        if request.method == 'POST':
            if 'add' in request.POST:
                form = TopicForm(request.POST)

                if form.is_valid():
                    topic = form.save(commit=False)
                    topic.customer = customer
                    topic.save()
            if 'delete_topic' in request.POST:
                topic_id = request.POST.get('topic_id')
                topic = get_object_or_404(Topic,id=topic_id)
                topic.delete()
                form = TopicForm()

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
            if 'add' in request.POST:
                form = QuestionForm(request.POST)

                if form.is_valid():
                    question = form.save(commit=False)
                    question.topic = topic
                    question.save()
            if 'delete_question' in request.POST:
                question_id = request.POST.get('question_id')
                question = get_object_or_404(Question, id= question_id)
                question.delete()

                form = TopicForm()


                

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







        
