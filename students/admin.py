from django.contrib import admin

from students.models.students import Student
from students.models.groups import Group

admin.site.register(Student)
admin.site.register(Group)
