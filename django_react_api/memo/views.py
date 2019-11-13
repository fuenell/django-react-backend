from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers, mixins, generics

from memo.models import Note


class MemoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'


@api_view(['GET'])
def get_note(request):
    notes = Note.objects.all()
    serializers = MemoSerializer(notes, many=True)
    return Response(serializers.data)


@api_view(['POST'])
def insert_note(request):
    serializers = MemoSerializer(data=request.data)
    if serializers.is_valid(raise_exception=True):
        serializers.save()
        return Response(serializers.data)


@api_view(['DELETE'])
def delete_note(self, request, *args, **kwargs):
    return self.destroy(request, *args, **kwargs)


# class MemoApi(GenericAPIView, mixins.ListModelMixin):
#     queryset = Note.objects.all()
#     serializer_class = MemoSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)


class NoteCollection(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     generics.GenericAPIView):
    queryset = Note.objects.all()
    serializer_class = MemoSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class NoteMember(mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 generics.GenericAPIView):
    queryset = Note.objects.all()
    serializer_class = MemoSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
