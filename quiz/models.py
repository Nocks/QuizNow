from django.db import models
from django.utils.text import slugify


class Exam(models.Model):
    """Details of an exam students will sit for."""
    name = models.CharField(max_length=200)
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE)
    institution = models.CharField(max_length=250)
    date_available = models.DateField()
    date_added = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    def __str__(self):
        return self.name

    def _get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        num = 1
        while Exam.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save()

    def get_absolute_url(self):
        return "/exam/{}/".format(self.slug)


class Subject(models.Model):
    """Subject details of the exam."""
    name = models.CharField(max_length=80, unique=True)

    def __str__(self):
        return self.name


class Question(models.Model):
    exam = models.ForeignKey(Exam,
                             on_delete=models.CASCADE,
                             related_name='questions')
    exam_question = models.CharField(max_length=600)

    def __str__(self):
        return self.exam_question


class Answer(models.Model):
    """Answers to questions."""
    question = models.ForeignKey(Question,
                             on_delete=models.CASCADE,
                             related_name='answers')
    question_answer = models.CharField(max_length=80, unique=True)
    correct_answer = models.BooleanField(default=False)

    def __str__(self):
        return self.question_answer
