from django.test import TestCase, Client
from django.urls import reverse
from .models import Post
from home.models import Documents, Aboutus, Banner, Collaborators, Consejos
from django.contrib.auth.models import User
from .forms import BannerForm, AboutUsForm
from django.contrib.auth.forms import AuthenticationForm

class PanelAdminViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.consejo = Consejos.objects.create(user=self.user)
        self.posts = Post.objects.create(user=self.user, title='Test Post', content='This is a test post')
        self.documents = Documents.objects.create(user=self.user, title='Test Document', pdf='test.pdf')
        self.banners = Banner.objects.create(user=self.user, image='test.jpg')
        self.aboutus = Aboutus.objects.create(user=self.user, content='This is a test about us')
        self.collaborators = Collaborators.objects.create(user=self.user, name='Test Name', image='test.jpg')

    def test_panel_admin_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('login:panel_admin'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'panel_admin.html')

class CreatePostViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.consejo = Consejos.objects.create(user=self.user)

    def test_create_post_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('login:create_post'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_form.html')

    def test_create_post_view_post(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('login:create_post'), {'title': 'Test Post', 'content': 'This is a test post'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login:panel_admin'))

class DeletePostViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.consejo = Consejos.objects.create(user=self.user)
        self.posts = Post.objects.create(user=self.user, title='Test Post', content='This is a test post')

    def test_delete_post_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('login:delete_post', args=[self.posts.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete.html')

    def test_delete_post_view_post(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('login:delete_post', args=[self.posts.id]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login:panel_admin'))

class UpdatePostViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.post = Post.objects.create(title='Test Post', content='This is a test post', user=self.user)

    def test_update_post_view(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('login:update_post', args=[self.post.id])
        response = self.client.post(url, {'title': 'Updated Post', 'content': 'This is an updated test post'})
        self.assertEqual(response.status_code, 302)
        updated_post = Post.objects.get(id=self.post.id)
        self.assertEqual(updated_post.title, 'Updated Post')
        self.assertEqual(updated_post.content, 'This is an updated test post')

class CreateDocumentViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_create_document_view(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('login:create_document')
        with open('test_document.pdf', 'rb') as f:
            response = self.client.post(url, {'title': 'Test Document', 'pdf': f})
        self.assertEqual(response.status_code, 302)
        new_document = Documents.objects.filter(user=self.user).last()
        self.assertEqual(new_document.title, 'Test Document')
        self.assertEqual(new_document.pdf.name.split('/')[-1], 'test_document.pdf')

class DeleteDocumentViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.document = Documents.objects.create(title='Test Document', user=self.user)

    def test_delete_document_view(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('login:delete_document', args=[self.document.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Documents.objects.filter(id=self.document.id).exists())

class CreateBannerViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        
    def test_create_banner_view_success(self):
        response = self.client.get(reverse('login:create_banner'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_form.html')
        
        banner_data = {
            'title': 'Test Banner',
            'image': 'test_image.jpg',
        }
        form = BannerForm(data=banner_data)
        self.assertTrue(form.is_valid())
        
        response = self.client.post(reverse('login:create_banner'), banner_data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'panel_admin.html')
        self.assertContains(response, 'Test Banner')
        
    def test_create_banner_view_max_reached(self):
        Banner.objects.create(title='Existing Banner', user=self.user)
        response = self.client.get(reverse('login:create_banner'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_form.html')
        
        banner_data = {
            'title': 'Test Banner',
            'image': 'test_image.jpg',
        }
        form = BannerForm(data=banner_data)
        self.assertTrue(form.is_valid())
        
        response = self.client.post(reverse('login:create_banner'), banner_data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_form.html')
        self.assertContains(response, 'Solamente puede añadir un Banner')
        
        
class DeleteBannerViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.banner = Banner.objects.create(title='Test Banner', user=self.user)
        self.client.login(username='testuser', password='testpass')
        
    def test_delete_banner_view_success(self):
        response = self.client.get(reverse('login:delete_banner', args=[self.banner.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete.html')
        self.assertContains(response, 'Test Banner')
        
        response = self.client.post(reverse('login:delete_banner', args=[self.banner.id]), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'panel_admin.html')
        self.assertNotContains(response, 'Test Banner')
        
    def test_delete_banner_view_wrong_user(self):
        other_user = User.objects.create_user(username='otheruser', password='otherpass')
        self.banner.user = other_user
        self.banner.save()
        
        response = self.client.post(reverse('login:delete_banner', args=[self.banner.id]), follow=True)
        self.assertEqual(response.status_code, 404)

class CreateAboutViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('create_about')
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

    def test_create_about_view_with_valid_form(self):
        response = self.client.post(self.url, {'field1': 'value1', 'field2': 'value2'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Aboutus.objects.filter(user=self.user).count(), 1)
    
    def test_create_about_view_with_existing_about(self):
        Aboutus.objects.create(user=self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Solamente puede añadir una descripción del consejo")
    
    def test_create_about_view_with_invalid_form(self):
        response = self.client.post(self.url, {'field1': 'value1'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Este campo es obligatorio")

class UpdateAboutViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.about = Aboutus.objects.create(user=self.user)
        self.url = reverse('update_about', args=[self.about.id])

    def test_update_about_view_with_valid_form(self):
        response = self.client.post(self.url, {'field1': 'new_value1', 'field2': 'new_value2'})
        self.assertEqual(response.status_code, 302)
        updated_about = Aboutus.objects.get(id=self.about.id)
        self.assertEqual(updated_about.field1, 'new_value1')
        self.assertEqual(updated_about.field2, 'new_value2')

    def test_update_about_view_with_invalid_form(self):
        response = self.client.post(self.url, {'field1': ''})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Este campo es obligatorio")

class SigninViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.signin_url = reverse('login:signin')
        self.user = User.objects.create_user(username='testuser', password='testpass')
    
    def test_signin_view_get(self):
        response = self.client.get(self.signin_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signin.html')
        self.assertIsInstance(response.context['form'], AuthenticationForm)
    
    def test_signin_view_post_success(self):
        data = {'username': 'testuser', 'password': 'testpass'}
        response = self.client.post(self.signin_url, data)
        self.assertRedirects(response, reverse('login:panel_admin'))
        self.assertTrue(response.wsgi_request.user.is_authenticated)
    
    def test_signin_view_post_failure(self):
        data = {'username': 'testuser', 'password': 'wrongpass'}
        response = self.client.post(self.signin_url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signin.html')
        self.assertIsInstance(response.context['form'], AuthenticationForm)
        self.assertContains(response, 'Usuario o Contraseña es incorrecto')

class SignoutViewTestCase(TestCase):  
    def setUp(self):
        self.client = Client()
        self.signout_url = reverse('logout:signout')
    
    def test_signout_view(self):
        response = self.client.get(self.signout_url)
        self.assertRedirects(response, reverse('home'))
        self

class CreateCollaboratorTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        
    def test_create_collaborator(self):
        response = self.client.post(reverse('create_collaborator'), {
            'name': 'Test Collaborator',
            'email': 'test@example.com',
            'phone': '555-555-5555',
            'photo': 'test.jpg',
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Collaborators.objects.filter(name='Test Collaborator').exists())

class DeleteCollaboratorTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.collaborator = Collaborators.objects.create(name='Test Collaborator', user=self.user)
        
    def test_delete_collaborator(self):
        response = self.client.post(reverse('delete_collaborator', args=[self.collaborator.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Collaborators.objects.filter(id=self.collaborator.id).exists())

class UpdateCollaboratorViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.collaborator = Collaborators.objects.create(user=self.user, name='Test Collaborator')
        self.url = reverse('update_collaborator', args=[self.collaborator.id])
        self.client.login(username='testuser', password='testpass')

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_form.html')
        self.assertIn('form', response.context)
        form = response.context['form']
        self.assertEqual(form.instance, self.collaborator)

    def test_post(self):
        data = {
            'name': 'Updated Collaborator Name',
            # include any other required fields in the data dictionary
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login:panel_admin'))
        self.collaborator.refresh_from_db()
        self.assertEqual(self.collaborator.name, 'Updated Collaborator Name')
        # assert that other fields were updated correctly as well

