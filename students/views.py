# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render

# Views for students
def students_list(request):
    students = (
        {'id': 1,
         'first_name': u'Корост',
         'last_name': u'Андрій',
         'ticket': 235,
         'image': 'img/me.jpeg'},
        {'id': 2,
         'first_name': u'Кот',
         'last_name': u'Семен',
         'ticket': 2123,
         'image': 'img/piv.png'},
        {'id': 3,
         'first_name': u'Джордан',
         'last_name': u'Майкл',
         'ticket': 2125,
         'image': 'img/piv.png'}
    )
    return render(request, 'students/students_list.html',
                  {'students': students})


def students_add(request):
    return HttpResponse('<h1>Student Add Form</h1>')


def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)


def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student</h1>' % sid)


# Views for groups
def groups_list(request):
    return HttpResponse('<h1>Groups Listing</h1>')


def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')


def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)


def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)


# Views for journal
def journal(request):
    return render(request, 'students/journal.html', {})
