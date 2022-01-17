from rest_framework import serializers
from core.models import Course, Module, Enrollment, Resource, resource


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = [
            'id',
            'title'
        ]


class ResourceEnrolledSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = [
            'id',
            'title',
            'description',
            'src',
            'type',
        ]


class ModuleSerializer(serializers.ModelSerializer):
    resources = serializers.SerializerMethodField()

    class Meta:
        model = Module
        fields = [
            'id',
            'title',
            'resources'
        ]

    def get_resources(self, obj):
        resources = obj.resources.filter(is_active=True)
        serializer = ResourceSerializer(instance=resources, many=True)
        return serializer.data

class ModuleEnrolledSerializer(serializers.ModelSerializer):
    resources = serializers.SerializerMethodField()

    class Meta:
        model = Module
        fields = [
            'id',
            'title',
            'resources'
        ]

    def get_resources(self, obj):
        resources = obj.resources.filter(is_active=True)
        serializer = ResourceEnrolledSerializer(instance=resources, many=True)
        return serializer.data

class CourseSerializer(serializers.ModelSerializer):
    modules = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = [
            'id', 
            'thumbnail', 
            'title', 
            'description',
            'price', 
            'is_free',
            'created_at',
            'modules'
        ]

    def get_modules(self, obj):
        modules = obj.modules.filter(is_active=True)
        serializer = ModuleSerializer(instance=modules, many=True)
        return serializer.data


class CourseDetailSerializer(serializers.ModelSerializer):
    modules = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = [
            'id', 
            'thumbnail', 
            'title', 
            'description', 
            'price',
            'thumbnail',
            'is_free',
            'created_at',
            'modules'
        ]

    def get_modules(self, obj):
        modules = obj.modules.filter(is_active=True)
        serializer = ModuleSerializer(instance=modules, many=True)
        return serializer.data


class CourseEnrolledSeralizer(serializers.ModelSerializer):
    modules = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = [
            'id', 
            'thumbnail', 
            'title', 
            'description',
            'thumbnail',
            'price',
            'is_free',
            'created_at',
            'modules',
        ]

    def get_modules(self, obj):
        modules = obj.modules.filter(is_active=True)
        serializer = ModuleEnrolledSerializer(instance=modules, many=True)
        return serializer.data


class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [
            'id',
            'title',
            'slug',
            'thumbnail',
            'description',
            'price'
        ]