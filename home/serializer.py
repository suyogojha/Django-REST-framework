from rest_framework import serializers
from .models import *
import re
from django.template.defaultfilters import slugify


class TodoSerializer(serializers.ModelSerializer):
    
    slug = serializers.SerializerMethodField()    
    
    class Meta:
        model = Todo
        fields = '__all__'
        # fields = ['todo_title'] # only todo_title field will be returned
        # exclude = ['created_at'] # exclude created_at field to use it other up fields should be commented

    #generate slug with rest framework
    def get_slug(self, obj):
        return slugify(obj.todo_title)  
        # return "test"  
        
        
        
        # to validate the data type 1
    def validate(self, validated_data):
        #print(validated_data)
        if validated_data.get('todo_title'):
            todo_title = validated_data['todo_title']
            regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
            
            if len(todo_title) < 5:
                raise serializers.ValidationError('Todo title should be atleast 5 characters long')
            
            if not regex.search(todo_title) == None:
                raise serializers.ValidationError(
                    'Todo title should be alphanumeric')
        return validated_data
    
        # to validate the data type 1
    # def validate_todo_title(self, data):
    #     #print(validated_data)
    #     if data:
    #         todo_title = data
    #         regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
            
    #         if len(todo_title) < 5:
    #             raise serializers.ValidationError('Todo title should be atleast 5 characters long')
            
    #         if not regex.search(todo_title) == None:
    #             raise serializers.ValidationError(
    #                 'Todo title should be alphanumeric')
    #     return data




#------------Default Router------------
class TimingTodoSerializer(serializers.ModelSerializer):
    todo = TodoSerializer()
    class Meta:
        model = TimingTodo
        fields = '__all__'
        #depth = 1