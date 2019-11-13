from django.urls import path
from rest_framework_swagger.views import get_swagger_view
from memo.views import NoteCollection, NoteMember

urlpatterns = [
    path('', NoteCollection.as_view()),
    path('note/', NoteCollection.as_view()),
    path('note/<int:pk>/', NoteMember.as_view()),
    path('docs/', get_swagger_view(title="API 문서"), name="swagger")
    # path('note/post/', NoteDetail.put),
    # path('note/delete/<int:pk>/', NoteDetail.delete),
    # path('<int:pk>/', views.DetailPost.as_view()),
]
