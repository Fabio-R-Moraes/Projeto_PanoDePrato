from django.test import TestCase
from panos_de_prato.models import Categoria, Panos, User


class PanosTestBase(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def faca_categoria(self, nome='Países'):
        return Categoria.objects.create(nome=nome)

    def faca_autor(
        self,
        first_name='Mariana',
        last_name='Moraes',
        username='maricotinha',
        password='fbrql823',
        email='maricota@gmail.com',
    ):
        return User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
            email=email,
        )

    def faca_pano(
        self,
        categoria_data=None,
        autor_data=None,
        titulo='Uruguai',
        descricao='País sul americano',
        slug='uruguai',
        preco=15,
        unidade_preco='Reais',
        esta_publicado=True,
    ):

        if categoria_data is None:
            categoria_data = {}

        if autor_data is None:
            autor_data = {}

        return Panos.objects.create(
            categoria=self.faca_categoria(**categoria_data),
            autor=self.faca_autor(**autor_data),
            titulo=titulo,
            descricao=descricao,
            slug=slug,
            preco=preco,
            unidade_preco=unidade_preco,
            esta_publicado=esta_publicado,
        )