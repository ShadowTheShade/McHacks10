import random;

from django.shortcuts import render

from django.urls import reverse_lazy #Interacting with the django shell from the server
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    )

from django.shortcuts import get_object_or_404, redirect

from .models import Question
from .forms import QuestionCheckForm


class QuestionListView(ListView):
    model = Question
    queryset = Question.objects.all().order_by("set", "-date_created")

#Uses django form to create a new question to be added to a pack
class QuestionCreateView(CreateView):
    model = Question
    fields = ["question", "answer", "option1", "option2", "option3", "option4", "set"]#
    success_url = reverse_lazy("question-list")

class QuestionUpdateView(QuestionCreateView, UpdateView):
    success_url = reverse_lazy("question-list")

#Subclass of QuestionListView
class SetView(QuestionListView):
    #Overwrite the default question_list.html
    template_name = "questions/set.html"
    form_class= QuestionCheckForm

    def get_queryset(self):
        return Question.objects.filter(set=self.kwargs["set_num"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["set_number"] = self.kwargs["set_num"]
        if self.object_list:
            context["check_question"]= random.choice(self.object_list)
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            question = get_object_or_404(Question, id=form.cleaned_data["card_id"])
            question.move(form.cleaned_data["solved"])

        return redirect(request.META.get("HTTP_REFERER"))

# def delete_object_function(request, id):
#     ob = Question.objects.get(id=id)
#     ob.delete()
#     return redirect('question-list')

class QuestionDeleteView(DeleteView):
    model = Question
    success_url = reverse_lazy("question-list")
