import uuid
from core.models import Order, Course
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, permissions
from .serializers import OrderGenerateSerializer


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def generate_order(request):
    if not request.query_params.get('course_id'):
        return Response(data={'detail': 'Please provide course_id'}, status=status.HTTP_400_BAD_REQUEST)
    course_id = request.query_params.get('course_id')
    try:
        course = Course.objects.get(id=course_id)
        order = Order(
            course=course, 
            price=float(course.price), 
            amount=float(course.price), 
            discount=0, 
            transaction_id=uuid.uuid4().hex
        )
        order.save()
        serializer = OrderGenerateSerializer(instance=order)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    except Course.DoesNotExist:
        return Response(data={'detail': 'Course not found'}, status=status.HTTP_404_NOT_FOUND)