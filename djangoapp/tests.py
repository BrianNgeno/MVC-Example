from django.test import TestCase
from .models import HomeInfo

# Create your tests here.
class HomeTestClass(TestCase):
    """
    Test homeinfo class and its functions
    """
    def setUp(self):
        #creating a new instance
        self.homeinfo = HomeInfo(title='informative', content='This is to explain on the MVC model', publisher="Brian",heading='MVC', time_created='2006-10-25')

    def test_instance(self):
        self.assertTrue(isinstance(self.homeinfo, HomeInfo))

    def test_save_method(self):
        """
        Function to test that info is being saved
        """
        self.homeinfo.save_info()
        homeinfo = HomeInfo.objects.all()
        self.assertTrue(len(homeinfo) > 0)

    def test_delete_method(self):
        """
        Function to test that a info can be deleted
        """
        self.homeinfo.save_info()
        self.homeinfo.del_info()

