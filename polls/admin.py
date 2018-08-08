

# Register your models here.

# -*- coding: utf-8 -*-

from __future__ import unicode_literals




from django.contrib import admin

from .models import Choice, Question


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
    

class QuestionAdmin(admin.ModelAdmin):
    # ...
    list_display = ('question_text', 'pub_date', 'was_published_recently')
	

admin.site.register(Question, QuestionAdmin)
