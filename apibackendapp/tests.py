from django.test import TestCase
from rest_framework.test import APITestCase,APIClient
from .models import Department,Employee
from datetime import date
from django.urls import reverse
from .serializers import EmployeeSerializer
from rest_framework import status


# Create your tests here.
#creating new employeeviewsettest class inheriting apitestcase class
class EmployeeViewSetTest(APITestCase):
    def setUp(self):
    #create a sample department object
     self.department = Department.objects.create(DepartmentName="HR")
    #create a sample employee object and assign the departments

     self.employee = Employee.objects.create(
            EmployeeName = "Jackie Chan",
            Designation = "Kungfu Master",
            DateOfJoining = date(2024, 11, 13),
            DepartmentId = self.department,
            Contact = "China",
            IsActive = True
        )
     #since we are testing APL, we need to create an APIClient object
     self.client = APIClient()

     #defining function to test employee listing api/endpoint

    def test_employee_list(self):
        #the default reverse url for listing modelname-list

        url = reverse('employee-list')
        response = self.client.get(url) #send api url and get response

        #get all employee objects
        employees = Employee.objects.all()
        #create a serializer object from EmployeeSerializer
        serializer = EmployeeSerializer(employees, many=True) #get all employees

        #check and compare response against setup data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        #check if status code is 200
        self.assertEqual(response.data, serializer.data)
        #check if seriali

        #test case2 to get particular employee details

    def test_employee_details(self):
        #the default reverse url for listing modelname-list

        url = reverse('employee-detail', args=[self.employee.EmployeeId])
        response = self.client.get(url) #send api url and get response

        #create serializer object from EmployeeSerializer using the setup data
        serializer = EmployeeSerializer(self.employee)#get employee details
       #check and compare response against the setup data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        #check if status code is 200
        self.assertEqual(response.data, serializer.data)
        #check if serializer data matches the actual data format

    

   


