from django.test import TestCase
from .models import Consejos, Banner, Aboutus, Collaborators, Documents
import datetime
from django.contrib.auth.models import User
# Create your tests here.

class ConsejosModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.consejo = Consejos.objects.create(name='testname', email='testemail', description='testdescription', type_consejo='Local', user=self.user)

    def test_consejos_name(self):
        consejo = Consejos.objects.get(id=1)
        self.assertEqual(consejo.name, 'testname')

    def test_consejos_email(self):
        consejo = Consejos.objects.get(id=1)
        self.assertEqual(consejo.email, 'testemail')

    def test_consejos_description(self):
        consejo = Consejos.objects.get(id=1)
        self.assertEqual(consejo.description, 'testdescription')

    def test_consejos_type_consejo(self):
        consejo = Consejos.objects.get(id=1)
        self.assertEqual(consejo.type_consejo, 'Local')

    def test_consejos_user(self):
        consejo = Consejos.objects.get(id=1)
        self.assertEqual(consejo.user, self.user)
        
        
class BannerModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.consejo = Consejos.objects.create(name='testname', email='testemail', description='testdescription', type_consejo='Local', user=self.user)
        self.banner = Banner.objects.create(image='testimage.jpg', consejo=self.consejo, user=self.user)

    def test_banner_image(self):
        banner = Banner.objects.get(id=1)
        self.assertEqual(banner.image, 'testimage.jpg')

    def test_banner_consejo(self):
        banner = Banner.objects.get(id=1)
        self.assertEqual(banner.consejo, self.consejo)

    def test_banner_user(self):
        banner = Banner.objects.get(id=1)
        self.assertEqual(banner.user, self.user)


class AboutusModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.consejo = Consejos.objects.create(name='testname', email='testemail', description='testdescription', type_consejo='Local', user=self.user)
        self.aboutus = Aboutus.objects.create(name='testname', description='testdescription', image='testimage.jpg', consejo=self.consejo, user=self.user)

    def test_aboutus_name(self):
        aboutus = Aboutus.objects.get(id=1)
        self.assertEqual(aboutus.name, 'testname')

    def test_aboutus_description(self):
        aboutus = Aboutus.objects.get(id=1)
        self.assertEqual(aboutus.description, 'testdescription')

    def test_aboutus_image(self):
        aboutus = Aboutus.objects.get(id=1)
        self.assertEqual(aboutus.image, 'testimage.jpg')

    def test_aboutus_consejo(self):
        aboutus = Aboutus.objects.get(id=1)
        self.assertEqual(aboutus.consejo, self.consejo)

    def test_aboutus_user(self):
        aboutus = Aboutus.objects.get(id=1)
        self.assertEqual(aboutus.user, self.user)


class CollaboratorsModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.consejo = Consejos.objects.create(name='testname', email='testemail', description='testdescription', type_consejo='Local', user=self.user)
        self.collaborator = Collaborators.objects.create(firstname='testfirstname', lastname='testlastname', position='testposition', description='testdescription', image='testimage.jpg', facebook='http://facebook.com', instagram='http://instagram.com', twitter='http://twitter.com', consejo=self.consejo, user=self.user)

    def test_collaborator_firstname(self):
        collaborator = Collaborators.objects.get(id=1)
        self.assertEqual(collaborator.firstname, 'testfirstname')

    def test_collaborator_lastname(self):
        collaborator = Collaborators.objects.get(id=1)
        self.assertEqual(collaborator.lastname, 'testlastname')

    def test_collaborator_position(self):
        collaborator = Collaborators.objects.get(id=1)
        self.assertEqual(collaborator.position, 'testposition')

    def test_collaborator_description(self):
        collaborator = Collaborators.objects.get(id=1)
        self.assertEqual(collaborator.description, 'testdescription')

    def test_collaborator_image(self):
        collaborator = Collaborators.objects.get(id=1)
        self.assertEqual(collaborator.image, 'testimage.jpg')

    def test_collaborator_facebook(self):
        collaborator = Collaborators.objects.get(id=1)
        self.assertEqual(collaborator.facebook, 'http://facebook.com')

    def test_collaborator_instagram(self):
        collaborator = Collaborators.objects.get(id=1)
        self.assertEqual(collaborator.instagram, 'http://instagram.com')

    def test_collaborator_twitter(self):
        collaborator = Collaborators.objects.get(id=1)
        self.assertEqual(collaborator.twitter, 'http://twitter.com')

    def test_collaborator_consejo(self):
        collaborator = Collaborators.objects.get(id=1)
        self.assertEqual(collaborator.consejo, self.consejo)

    def test_collaborator_user(self):
        collaborator = Collaborators.objects.get(id=1)
        self.assertEqual(collaborator.user, self.user)


class DocumentsModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Crear un usuario y un consejo para el test
        user = User.objects.create(username='testuser')
        consejo = Consejos.objects.create(name='Consejo de prueba', user=user)
        # Crear un documento para el test
        Documents.objects.create(title='Documento de prueba', pdf='document.pdf', date=datetime.datetime.now(), consejo=consejo, user=user)

    def test_title_max_length(self):
        document = Documents.objects.get(id=1)
        max_length = document._meta.get_field('title').max_length
        self.assertEquals(max_length, 100)

    def test_description_max_length(self):
        document = Documents.objects.get(id=1)
        max_length = document._meta.get_field('description').max_length
        self.assertEquals(max_length, 500)

    def test_date_auto_now_add(self):
        document = Documents.objects.get(id=1)
        self.assertIsNotNone(document.date)

    def test_consejo_relationship(self):
        document = Documents.objects.get(id=1)
        consejo = document.consejo
        self.assertEquals(consejo.name, 'Consejo de prueba')