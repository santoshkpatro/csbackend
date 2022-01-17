from rest_framework import generics, permissions
from .serializers import CourseSerializer, CourseDetailSerializer, CourseEnrolledSeralizer, CourseListSerializer
from core.models import Course


class CourseListView(generics.ListAPIView):
    serializer_class = CourseListSerializer
    queryset = Course.objects.all()


class CourseDetailView(generics.RetrieveAPIView):
    enrolled_serializer_class = CourseEnrolledSeralizer
    auth_serializer_class = CourseDetailSerializer
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def get_serializer_class(self):
        if bool(self.request.user and self.request.user.is_authenticated):
            instance = self.get_object()
            if instance in Course.objects.filter(enrollments__user=self.request.user, enrollments__is_active=True):
                return self.enrolled_serializer_class
            return self.auth_serializer_class
        return super().get_serializer_class()