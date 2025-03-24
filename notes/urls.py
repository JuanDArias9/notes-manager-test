from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import NoteViewSet
from .views import notes_view

router = DefaultRouter()
router.register('api/notes', NoteViewSet, 'notes')

urlpatterns = [
    path('', notes_view, name='notes'),
    path('', include(router.urls)),  
]
