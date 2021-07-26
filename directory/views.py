import csv
import os
import zipfile

from django.conf import settings
from django.shortcuts import render

from directory.models import Teacher
from directory.forms import SearchForm, BulkUploadForm


def upload_teachers_from_csv(profiles_csv_file, images_zip_file):
    bytes_csv_content = profiles_csv_file.file.read()
    text_csv_content = bytes_csv_content.decode('UTF-8').splitlines()
    reader = csv.DictReader(text_csv_content)
    if images_zip_file is not None and zipfile.is_zipfile(images_zip_file):
        with zipfile.ZipFile(images_zip_file) as zfile:
            for t in reader:
                if not t['Email Address']:
                    continue
                new_teacher = Teacher(
                    first_name=t['First Name'],
                    last_name=t['Last Name'],
                    email=t['Email Address'],
                    phone_number=t['Phone Number'],
                    room_number=t['Room Number'],
                )
                new_teacher.save()
                new_teacher.subjects = t['Subjects taught']
                new_teacher.save()
                if t['Profile picture'] not in zfile.namelist():
                    with open(os.path.join(settings.MEDIA_ROOT,
                                           'profile_images',
                                           'placeholder.png'), 'rb') as profile_picture_file:
                        new_teacher.profile_picture.save('placeholder.png',
                                                         profile_picture_file,
                                                         True)
                else:
                    with zfile.open(
                            t['Profile picture']) as profile_picture_file:
                        new_teacher.profile_picture.save(t['Profile picture'],
                                                         profile_picture_file,
                                                         True)


# Create your views here.

def index(request):
    search_form = SearchForm()
    teachers = Teacher.objects.all()
    bulk_upload_form = BulkUploadForm()
    if request.method == 'POST':
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            conditions = {}
            subject = search_form.cleaned_data['subject']
            first_letter_of_last_name = search_form.cleaned_data[
                'first_letter_of_last_name']
            if subject:
                conditions['_subjects__pk'] = subject
            if first_letter_of_last_name:
                conditions['last_name__startswith'] = first_letter_of_last_name
            teachers = Teacher.objects.filter(**conditions)
    context = {"teachers": teachers,
               "search_form": search_form,
               "bulk_upload_form": bulk_upload_form}
    return render(request, 'index.html', context=context)


def teacher(request, teacher_id):
    # TODO(*): Add not found exception handling.
    context = {"teacher": Teacher.objects.get(pk=teacher_id)}
    return render(request, 'teacher.html', context=context)


def bulk_upload(request):
    search_form = SearchForm()
    teachers = Teacher.objects.all()
    bulk_upload_form = BulkUploadForm()
    context = {"teachers": teachers,
               "search_form": search_form,
               "bulk_upload_form": bulk_upload_form}
    if request.method == 'POST':
        bulk_upload_form = BulkUploadForm(request.POST, request.FILES)
        if bulk_upload_form.is_valid():
            upload_teachers_from_csv(request.FILES['csv_file'],
                                     request.FILES['images_archive'])
    return render(request, 'index.html', context=context)
