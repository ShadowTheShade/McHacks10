from django import template

from questions.models import SETS, Question

#Creates an instance of Library used for registering the template tags
register = template.Library()

#To be included in navigation.html
@register.inclusion_tag("questions/set_links.html")
def sets_as_links():
    sets = []
    #Iterates from 1 to the number of sets(+1)
    for set_num in SETS:
        #Filters the objects by set type and counts them
        question_count = Question.objects.filter(set=set_num).count()
        #Adding a dict entry to the array of sets
        sets.append({
            "number": set_num,
            "question_count": question_count,
        })
    #Returns a dict with the data from the sets
    return {"sets": sets}