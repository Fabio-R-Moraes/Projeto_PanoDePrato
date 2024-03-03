from django.test import TestCase
from django.urls import reverse, resolve
from panos_de_prato import views

class PanosViewsTest(TestCase):
    def test_panos_home_view_esta_correta(self):
        view = resolve(reverse('panos-home'))
        self.assertIs(view.func, views.home)

    def test_panos_categoria_view_esta_correta(self):
        view = resolve(reverse('categoria', kwargs={'categoria_id':1}))
        self.assertIs(view.func, views.categoria)

    def test_pannos_pano_view_esta_correta(self):
        view = resolve(reverse('panos-pano', kwargs={'id':1}))
        self.assertIs(view.func, views.pano)