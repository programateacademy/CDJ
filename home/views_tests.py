from django.urls import reverse
from django.test import Client, TestCase
from .models import Consejos
from login.models import Post

class HomeViewTestCase(TestCase):
    def setUp(self):
        Consejos.objects.create(type_consejo='Curul', title='Curul Consejo')
        Consejos.objects.create(type_consejo='Local', title='Local Consejo')
        Post.objects.create(title='First post', content='Lorem ipsum dolor sit amet')

    def test_home_view_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_view_template_used(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')

    def test_home_view_context_data(self):
        response = self.client.get(reverse('home'))
        self.assertTrue('consejos' in response.context)
        self.assertTrue('latest_post' in response.context)
        self.assertTrue('all_posts' in response.context)
        self.assertEqual(len(response.context['consejos']), 2)
        self.assertEqual(response.context['latest_post'].title, 'First post')
        self.assertEqual(len(response.context['all_posts']), 0)

class CurulConsejosViewTestCase(TestCase):
    def setUp(self):
        Consejos.objects.create(type_consejo='Curul', title='Curul Consejo')
        Consejos.objects.create(type_consejo='Local', title='Local Consejo')

    def test_curul_consejos_view_status_code(self):
        response = self.client.get(reverse('curul_consejos'))
        self.assertEqual(response.status_code, 200)

    def test_curul_consejos_view_template_used(self):
        response = self.client.get(reverse('curul_consejos'))
        self.assertTemplateUsed(response, 'consejos_locales.html')

    def test_curul_consejos_view_queryset(self):
        response = self.client.get(reverse('curul_consejos'))
        curul_consejos = response.context['curul_consejos']
        self.assertEqual(len(curul_consejos), 1)
        self.assertEqual(curul_consejos[0].title, 'Curul Consejo')

class ConsejosLocalesViewTestCase(TestCase):
    def setUp(self):
        Consejos.objects.create(type_consejo='Curul', title='Curul Consejo')
        Consejos.objects.create(type_consejo='Local', title='Local Consejo')

    def test_consejos_locales_view_status_code(self):
        response = self.client.get(reverse('consejos_locales'))
        self.assertEqual(response.status_code, 200)

    def test_consejos_locales_view_template_used(self):
        response = self.client.get(reverse('consejos_locales'))
        self.assertTemplateUsed(response, 'consejos_locales.html')

    def test_consejos_locales_view_queryset(self):
        response = self.client.get(reverse('consejos_locales'))
        consejos_locales = response.context['consejos_locales']
        self.assertEqual(len(consejos_locales), 1)
        self.assertEqual(consejos_locales[0].title, 'Local Consejo')

class SearchConsejosViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.consejo_local = Consejos.objects.create(
            name='Consejo Local de prueba',
            type_consejo='Local',
            description='Descripción de prueba',
            email='prueba@consejolocal.com',
            logo='logo.jpg'
        )

    def test_search_consejos(self):
        response = self.client.get(reverse('search_consejos'), {'q': 'prueba'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()['results']), 1)
        self.assertEqual(response.json()['results'][0]['name'], 'Consejo Local de prueba')

class DetalleConsejoViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.consejo = Consejos.objects.create(
            name='Consejo de prueba',
            type_consejo='Curul',
            description='Descripción de prueba',
            email='prueba@consejo.com',
            logo='logo.jpg'
        )

    def test_detalle_consejo(self):
        response = self.client.get(reverse('detalle_consejo', args=[self.consejo.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'council.html')
        self.assertEqual(response.context['consejo'], self.consejo)

