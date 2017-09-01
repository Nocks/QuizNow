from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.base import RedirectView
from django.views.generic import ListView

from quiz.models import Exam, Question, Answer


class IndexView(TemplateView):
    template_name = 'quiz/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['exams'] = Exam.objects.all()
        return context


class ExamDetailView(DetailView):
    model = Exam
    template_name = 'quiz/exam_details.html'


class QuizView(DetailView):
    model = Exam
    template_name = 'quiz/quiz.html'


    def get_context_data(self, **kwargs):
        context = super(QuizView, self).get_context_data(**kwargs)
        context['exam'] = Exam.objects.filter(slug=self.kwargs['slug'])
        return context


class ExamRedirectView(RedirectView):
    url = '/'
