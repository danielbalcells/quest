from django.urls import path

from backend import views


urlpatterns = [
    path('questions/', views.question_list,
         name='question-list'),
    path('questions/<int:id>/', views.question_detail,
         name='question-detail'),
    path('questions/<int:id>/links',
         views.question_outgoing_links_list,
         name='question-outgoing-links-list'),
    path('questions/<int:id>/linked-questions',
         views.question_linked_questions,
         name='question-linked-questions'),
    path('links/', views.question_link_list,
         name='question-link-list'),
    path('links/<int:id>/', views.question_link_detail,
         name='question-link-detail'),
]
