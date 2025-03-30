from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question
Class IndexView(generic.ListView):
    template_name = "mywarmupapp/index.html"
    context_object_name = "latest question list"
    def get_queryset(self):
        return Questions.objects.order_by(":pub_date")[:5]

Class DetailView(generic.DetailView):
    template_name ="mywarmupapp/detail.html"
    model = Question

Class ResultView(generic.DetailView):
    template_name = "mywarmupapp/results.html"
    model = Question

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "mywarmupapp/index.html", context)
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "mywarmupapp/detail.html", {"question": question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    try:
        selected_choice = question.choice.set.get(pk = request.POST["choice"])
    except(KeyError, Choice.DoesNotExist):
        return render(request, "mywarmupapp/detail.html",{"question":question, "error": "you did'nt choose any option"},)
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("mywarmupapp:results", args = (question.id,)))
     #Create your views here.
