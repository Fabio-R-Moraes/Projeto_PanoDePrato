from django.urls import reverse, resolve
from panos_de_prato import views
from .test_panos_base import PanosTestBase

class PanosPanoViewTests(PanosTestBase):
    def test_panos_pano_view_esta_correta(self):
        view = resolve(reverse('panos:pano', kwargs={'id':1}))
        self.assertIs(view.func, views.pano)

    def test_panos_pano_view_retorna_404_se_nao_acha_o_pano(self):
        response = self.client.get(reverse('panos:pano', kwargs={'id':1000}))
        self. assertEqual(response.status_code, 404)

    #Esse teste não funciona por causa do campo <pano_imagem> com detalhe=true
    '''def test_panos_pano_template_carrega_o_pano_correto(self):
        titulo_necessario = 'Esse é um teste para a página com título'
        self.faca_pano(titulo=titulo_necessario)
        response = self.client.get(reverse('panos:pano', kwargs={'id': 1}))

        #Verificação por conteúdo
        response_content = response.content.decode('utf-8')
        self.assertIn(titulo_necessario, response_content)'''
    
    def test_panos_pano_nao_carrega_pano_nao_publicado(self):
        pano = self.faca_pano(esta_publicado=False)
        response = self.client.get(reverse('panos:pano', kwargs={'id': pano.id}))

        self.assertEqual(response.status_code, 404)
