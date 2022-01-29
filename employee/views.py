from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from employee.models import Employee
from employee.serializers import EmployeeSerializer
from rest_framework.viewsets import ModelViewSet
# from rest_framework.mixins import RetrieveModelMixin,DestroyModelMixin
#
# class MyOwnViewSet(GenericViewSet,RetrieveModelMixin,DestroyModelMixin):
#     pass

class EmployeeOperations(ModelViewSet):
    queryset = Employee.objects.all() # to retrive all the records
    serializer_class = EmployeeSerializer
        