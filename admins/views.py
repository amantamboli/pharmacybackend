from django.http import JsonResponse
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from .models import userAdmin
from admins.serializers import Adminserializer,updateAdminserializer
from rest_framework import generics, status

# class UserAdminCreateView(generics.CreateAPIView):
#     queryset = userAdmin.objects.all()
#     serializer_class = Adminserializer

#     def create(self, request, *args, **kwargs):
#         # Validate if name already exists
#         name = request.data.get('name')
#         if userAdmin.objects.filter(name=name).exists():
#             return Response(
#                 {'warning': 'User with this name already exists.'},
#                 status=status.HTTP_400_BAD_REQUEST
#             )

#         # Continue with the regular create process
#         response = super().create(request, *args, **kwargs)
#         response.data['message'] = 'User created successfully'
#         return response


class UserAdminCreateView(generics.CreateAPIView):
    queryset = userAdmin.objects.all()
    serializer_class = Adminserializer

    def create(self, request, *args, **kwargs):
        # Create a mutable copy of the request data
        request_data = request.data.copy()

        # Hash the user's password before saving
        request_data['password'] = make_password(request_data.get('password'))

        # Validate if name already exists
        name = request_data.get('name')
        if userAdmin.objects.filter(name=name).exists():
            return Response(
                {'warning': 'User with this name already exists.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Explicitly create the user with the hashed password
        serializer = self.get_serializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # Modify the response to exclude sensitive information
        response_data = {'message': 'User created successfully'}
        return Response(response_data, status=status.HTTP_201_CREATED)
    
class UserAdminListView(generics.ListAPIView):
    queryset = userAdmin.objects.all()
    serializer_class = Adminserializer



class UserAdminDestroyView(generics.DestroyAPIView):
    queryset = userAdmin.objects.all()
    serializer_class = updateAdminserializer
    lookup_field = 'name'

    def get_object(self):
        name = self.kwargs.get(self.lookup_field)
        try:
            return self.queryset.get(name=name)
        except userAdmin.DoesNotExist:
            raise generics.Http404(f"User with name {name} not found.")


    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()

            # Add any custom validation or checks before deletion if needed
            # For example, you might want to check if the user has the right permissions.

            # Continue with the regular destroy process
            self.perform_destroy(instance)

            return Response({'message': 'User deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

        except generics.Http404 as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
        
        

class UserAdminUpdateView(generics.UpdateAPIView):
    queryset = userAdmin.objects.all()
    serializer_class = Adminserializer
    lookup_field = 'name'

    def get_object(self):
        name = self.kwargs.get(self.lookup_field)
        try:
            return self.queryset.get(name=name)
        except userAdmin.DoesNotExist:
            raise generics.Http404(f"User with name {name} not found.")

    def update(self, request, *args, **kwargs):
        instance = self.get_object()

        serializer = self.get_serializer(instance, data=request.data,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'message': 'User updated successfully'}, status=status.HTTP_200_OK)
    
