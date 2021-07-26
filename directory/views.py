from django.shortcuts import render

from directory.models import Teacher
from directory.forms import SearchForm


# Create your views here.

def index(request):
    form = SearchForm()
    teachers = Teacher.objects.all()
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            conditions = {}
            subject = form.cleaned_data['subject']
            first_letter_of_last_name = form.cleaned_data['first_letter_of_last_name']
            if subject:
                conditions['_subjects__pk'] = subject
            if first_letter_of_last_name:
                conditions['last_name__startswith'] = first_letter_of_last_name
            teachers = Teacher.objects.filter(**conditions)
    context = {"teachers": teachers,
               "form": form}
    return render(request, 'index.html', context=context)


def teacher(request, teacher_id):
    # TODO(*): Add not found exception handling.
    context = {"teacher": Teacher.objects.get(pk=teacher_id)}
    return render(request, 'teacher.html', context=context)


