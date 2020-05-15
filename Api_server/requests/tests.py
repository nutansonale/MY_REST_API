from django.test import TestCase
from requests.models import ProjectCreateQ

# Create your tests here.
class ModelTest(TestCase,):

    def test_object(self):
        sid=123
        user='nutan'
        dock='imag1'
        status=True
        obj=ProjectCreateQ(sid=sid,user_name=user,dimage=dock,status=status)
        self.assertEqual(obj.dimage,dock)