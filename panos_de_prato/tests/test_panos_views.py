from django.test import TestCase
from django.urls import reverse, resolve
from panos_de_prato import views
from panos_de_prato.models import Panos, Categoria, User

class PanosViewsTest(TestCase):
    def test_panos_home_view_esta_correta(self):
        view = resolve(reverse('panos:home'))
        self.assertIs(view.func, views.home)

    def test_panos_categoria_view_esta_correta(self):
        view = resolve(reverse('panos:categoria', kwargs={'categoria_id':1}))
        self.assertIs(view.func, views.categoria)

    def test_panos_pano_view_esta_correta(self):
        view = resolve(reverse('panos:pano', kwargs={'id':1}))
        self.assertIs(view.func, views.pano)

    def test_panos_categoria_view_retorna_404_se_nao_acha_o_pano(self):
        response = self.client.get(reverse('panos:categoria', kwargs={'categoria_id':1000}))
        self.assertEqual(response.status_code, 404)

    def test_panos_pano_view_retorna_404_se_nao_acha_o_pano(self):
        response = self.client.get(reverse('panos:pano', kwargs={'id':1000}))
        self. assertEqual(response.status_code, 404)

    def test_panos_procurar_usando_a_view_correta(self):
        resolved = resolve(reverse('panos:procurar'))
        self.assertIs(resolved.func, views.procurar)

    def test_panos_procurar_carrega_o_template_correto(self):
        view = self.client.get(reverse('panos:procurar') + '?q=teste')
        self.assertTemplateUsed(view, 'procurar.html')
        
    def test_panos_procura_sem_termo_levanta_um_404(self):
        url = reverse('panos:procurar')
        print(f'Resposta: {url}')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)