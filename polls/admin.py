from django.contrib import admin
from .models import Question,Choice

admin.site.register(Choice)   

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]    
    list_display = ["question_text", "pub_date"]
 
admin.site.register(Question, QuestionAdmin)
