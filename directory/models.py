from django.db import models


class Subject(models.Model):
    subject_name = models.CharField(unique=True, primary_key=True,
                                    max_length=40)


class Teacher(models.Model):
    first_name = models.CharField(max_length=200, verbose_name="First Name")
    last_name = models.CharField(max_length=200, verbose_name="Last Name")
    profile_picture = models.ImageField(upload_to="profile_images/",
                                        verbose_name="Profile picture")
    email = models.EmailField(verbose_name="Email", unique=True)
    phone_number = models.CharField(max_length=25, verbose_name="Phone number")
    room_number = models.CharField(max_length=10, verbose_name="Room number")
    _subjects = models.ManyToManyField(Subject, db_column="subjects")

    @property
    def subjects(self):
        return ", ".join(self._subjects.values_list("subject_name", flat=True))

    @subjects.setter
    def subjects(self, value):
        if not value:
            self._subjects.clear()
        else:
            for subject_name in map(lambda x: x.strip().title(),
                                    value.split(",")):
                subject, created = \
                    Subject.objects.get_or_create(subject_name=subject_name)
                if created:
                    subject.save()
                self._subjects.add(subject)

    def __repr__(self):
        return f"{self.first_name} {self.last_name}: {self.email}"


