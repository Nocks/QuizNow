from django.conf.urls import url

from quiz.views import ExamDetailView, QuizView

urlpatterns = [
    url(r'^(?P<slug>[\w-]+)/$', ExamDetailView.as_view(), name='exam'),
    url(r'^quiz/(?P<slug>[\w-]+)/$', QuizView.as_view(), name='take_quiz'),
]
