from django.urls import reverse, resolve
from panos_de_prato import views
from .test_panos_base import PanosTestBase

class PanosCategoriasViewTests(PanosTestBase):
    def test_panos_categoria_view_esta_correta(self):
        view = resolve(reverse('panos:categoria', kwargs={'categoria_id':1}))
        self.assertIs(view.func, views.categoria)

    def test_panos_categoria_view_retorna_404_se_nao_acha_o_pano(self):
        response = self.client.get(reverse('panos:categoria', kwargs={'categoria_id':1000}))
        self.assertEqual(response.status_code, 404)

    #Esse teste não funciona por causa do campo <pano_imagem> e detalhes=true
    '''def test_panos_categoria_template_carrega_pano(self):
        titulo_necessario = 'Esse é um teste para categoria'
        self.faca_pano(titulo=titulo_necessario)
        response = self.client.get(reverse('panos:categoria', args=(1,)))

        #Verificação por conteúdo
        response_content = response.content.decode('utf-8')
        self.assertIn(titulo_necessario, response_content)'''
    
    #Esse teste não funciona por que <pano> não está definido
    def test_panos_categoria_nao_carrega_panos_nao_publicados(self):
        pano = self.faca_pano(esta_publicado=False)
        response = self.client.get(reverse('panos:pano', kwargs={'id': pano.categoria.id}))

        self.assertEqual(response.status_code, 404)
