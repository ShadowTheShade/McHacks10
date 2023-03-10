from django.urls import path

from . import views

urlpatterns = [

    path(
        "",
        views.QuestionListView.as_view(),
        name="question-list"
    ),
    path(
        "new",
        views.QuestionCreateView.as_view(),
        name="question-create"
    ),
    path(
        "edit/<int:pk>",
        views.QuestionUpdateView.as_view(),
        name="question-update"
    ),
    path(
        "set/<int:set_num>",
        views.SetView.as_view(),
        name="set"
    ),
    
    # path('obj-del/<int:id>', 
    # views.delete_object_function, 
    # name='obj-del'),

    path('<pk>/obj-del', 
    views.QuestionDeleteView.as_view(),
    name='obj-del'),
    
]