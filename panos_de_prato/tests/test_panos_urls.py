from django.test import TestCase
from django.urls import reverse

class PanosURLSTest(TestCase):
    def test_panos_home_url_esta_correta(self):
        url = reverse('panos:home')
        self.assertEqual(url, '/')
        
    def test_panos_categoria_url_esta_correta(self):
        url = reverse('panos:categoria', kwargs={'categoria_id':1})
        self.assertEqual(url, '/panos_de_prato/categoria/1/')

    def test_panos_pano_url_esta_correta(self):
        url = reverse('panos:pano', kwargs={'id':1})
        self.assertEqual(url, '/panos_de_prato/1/')

    def test_panos_procurar_url_esta_correta(self):
        url = reverse('panos:procurar')
        self.assertEqual(url, '/panos_de_prato/procurar/')