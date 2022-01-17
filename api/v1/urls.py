from django.urls import path
from .courses.views import CourseDetailView, CourseListView
from .orders.views import generate_order

urlpatterns = [
    # courses
    path('courses/', CourseListView.as_view()),
    path('courses/<uuid:pk>/', CourseDetailView.as_view()),

    # orders
    path('orders/generate/', generate_order),
]