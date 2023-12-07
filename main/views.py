from rest_framework import generics, permissions
from .models import Contact
from .serializers import ContactSerializer
from rest_framework.response import Response
from rest_framework import status

# List = "get"
# Create = "post"
# APIView = "generics"

class ContactListCreateAPIView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    search_fields = ['name', 'email']
    ordering_fields = ['name', 'email', 'phone']
    
    def get_queryset(self):
        # Создаём запрос на получение всех объектов модели Contact
        queryset = Contact.objects.all()
        # Получаем значение параметра search из запроса и фильтруем запрос 
        # на поиск по имени или по email. Если значение search отсутствует, будет None.
        search_term = self.request.query_params.get('search', None)
        # Если значение search не None, то фильтруем запрос и возвращаем результат запроса
        if search_term:
            queryset = queryset.filter(name__icontains=search_term) |\
                       queryset.filter(email__icontains=search_term)
        return queryset
    
    def post(self, request, *args, **kwargs):
        if len(request.data.get('name', '')) < 10:
            return Response(
                {'error': 'Имя не может быть меньше 10 символов.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        else:
            return super().post(request, *args, **kwargs)

class ContactRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'
    