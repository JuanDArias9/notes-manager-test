from rest_framework import viewsets, permissions
from .models import Note
from .serializers import NoteSerializer


class NoteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Note.objects.all().order_by("-created_at")
    permission_classes = [permissions.AllowAny]
    serializer_class = NoteSerializer
