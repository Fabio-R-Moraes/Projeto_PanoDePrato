from unittest import TestCase
from paginacao import make_pagination_range

class PaginacaoTeste(TestCase):
    def test_fazer_um_range_de_paginacao_retornar_um_range_de_paginacao(self):
        paginacao = make_pagination_range(
            range_pagina = list(range(1,21)),
            qtd_paginas = 4,
            pagina_atual = 1,
        )['paginacao']

        self.assertEqual([1,2,3,4], paginacao)

    def test_faca_o_range_do_meio_ficar_correto(self):
        paginacao = make_pagination_range(
            range_pagina = list(range(1,21)),
            qtd_paginas = 4,
            pagina_atual = 10,
        )['paginacao']

        self.assertEqual([9,10,11,12], paginacao)

    def test_range_de_paginacao_estatico_se_a_ultima_pagina_estiver_no_range(self): #  noqa E501
        paginacao = make_pagination_range(
            range_pagina = list(range(1,21)),
            qtd_paginas = 4,
            pagina_atual = 18,
        )['paginacao']

        self.assertEqual([17,18,19,20], paginacao)
