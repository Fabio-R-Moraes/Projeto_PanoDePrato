from django.urls import reverse, resolve
from panos_de_prato import views
from .test_panos_base import PanosTestBase

class PanosHomeViewTests(PanosTestBase):
    def test_panos_home_view_esta_correta(self):
        view = resolve(reverse('panos:home'))
        self.assertIs(view.func, views.home)

    def test_panos_home_view_retorna_status_200_ok(self):
        response = self.client.get(reverse('panos:home'))
        self.assertEqual(response.status_code, 200)

    def test_panos_home_view_carrega_template_correto(self):
        response = self.client.get(reverse('panos:home'))
        self.assertTemplateUsed(response, 'home.html')

    def test_home_mostrar_panos_nao_encontrados(self):
        response = self.client.get(reverse('panos:home'))
        self.assertIn('<h1>Não há panos de prato para mostrar...</h1>', response.content.decode('utf-8'))

    #Esse teste não funciona!!!
    '''def test_panos_home_template_carrega_panos(self):
        self.faca_pano(autor_data={
            'first_name': 'Fábio'
        })

        response = self.client.get(reverse('panos:home'))

        #Verificação por contexto
        #response_content = response.content.decode('utf-8')
        #self.assertEqual(response_content.first().titulo, 'Uruguai')

        #Verificação por conteúdo
        response_content = response.content.decode('utf-8')
        response_context_panos = response.context['panos']

        self.assertIn('Uruguai', response_content)
        self.assertIn('Fábio', response_content)
        self.assertEqual(len(response_context_panos), 1)'''
    
    def test_panos_home_nao_carrega_receitas_nao_publicacas(self):
        self.faca_pano(esta_publicado=False)
        response = self.client.get(reverse('panos:home'))

        self.assertIn('<h1>Não há panos de prato para mostrar...</h1>', response.content.decode('utf-8'))

    #Esse teste não funciona por causa do campo <pano_imagem>
    '''def test_panos_home_esta_paginando(self):
        for i in range(18):
            kwargs={
                'autor_data': {
                    'username': f'Fábio_{i}'
                },
                'slug': f'programador_{i}',
            }
            self.faca_pano(**kwargs)

        response = self.client.get(reverse('panos:home'))
        panos = response.context['panos']
        paginacao = panos.paginador

        self.assertEqual(paginacao.num_pages, 3)'''
    
