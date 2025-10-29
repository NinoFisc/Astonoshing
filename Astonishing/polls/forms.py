from django import forms
from .models import Question, Topic




class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['name','description']

