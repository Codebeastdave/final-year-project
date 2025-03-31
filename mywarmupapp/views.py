from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import F
from django.urls import reverse
from django.views import generic
from .models import Question, Choice
class IndexView(generic.ListView):
    template_name = "mywarmupapp/index.html"
    context_object_name = "latest_question_list"
    def get_queryset(self):
        return Question.objects.order_by("pub_date")[:5]

class DetailView(generic.DetailView):
    template_name ="mywarmupapp/detail.html"
    model = Question

class ResultView(generic.DetailView):
    template_name = "mywarmupapp/results.html"
    model = Question

def vote(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    try:
        print(50)
        selected_choice = question.choice_set.get(pk = request.POST["choice"])
    except(KeyError, Choice.DoesNotExist):
        print(89)
        return render(request, "mywarmupapp/detail.html",{"question":question, "error": "you did'nt choose any option"},)
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("mywarmupapp:results", args = (question.id,)))
     #Create your views here.
