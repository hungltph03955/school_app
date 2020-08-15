from django.urls import path

from . import views

urlpatterns = [
    path('subject/list/', views.SubjectListView.as_view(), name='subjects'),
    # path('subject/create/', views.SubjectCreateView.as_view(), name='subject-create'),
    # path('subject/<int:pk>/update/', views.SubjectUpdateView.as_view(), name='subject-update'),
    # path('subject/<int:pk>/delete/', views.SubjectDeleteView.as_view(), name='subject-delete'),
]
