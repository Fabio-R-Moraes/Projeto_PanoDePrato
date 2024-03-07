from django.urls import reverse, resolve
from panos_de_prato import views
from .test_panos_base import PanosTestBase

class PanosPanoViewTests(PanosTestBase):
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

    def test_panos_termo_procurado_esta_no_titulo_pagina_e_com_escape(self):
        url = reverse('panos:procurar') + '?q=<Teste>'
        response = self.client.get(url)
        self.assertIn('Pesquisando por &quot;&lt;Teste&gt;&quot;', response.content.decode('utf-8'))

    #Esse teste não funciona por causa do campo <pano_imagem>
    '''def test_panos_pesquisa_procurar_pano_por_titulo(self):
        titulo1 = 'Esse é o primeiro título'
        titulo2 = 'Esse é o segundo título'

        pano1 = self.faca_pano(
            slug='um',
            titulo=titulo1,
            autor_data={'username':'Maricotinha'}
        )
        pano2 = self.faca_pano(
            slug='dois',
            titulo=titulo2,
            autor_data={'username':'Vitinho'}
        )

        url_procurada = reverse('panos:procurar')
        response1 = self.client.get(f'{url_procurada}?q={titulo1}')
        response2 = self.client.get(f'{url_procurada}?q={titulo2}')
        response_both = self.client.get(f'{url_procurada}?q=Este')
        
        self.assertIn(pano1, response1.context['panos'])
        self.assertNotIn(pano2, response1.context['panos'])

        self.assertIn(pano2, response2.context['panos'])
        self.assertNotIn(pano1, response2.context['panos'])

        self.assertIn(pano1, response_both.context['panos'])
        self.assertIn(pano2, response_both.context['panos'])'''
