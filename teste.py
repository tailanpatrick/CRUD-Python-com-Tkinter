from model.produtoDAO import ProdutoDAO
from model.produto import Produto

produtoDao = ProdutoDAO()
produto = Produto("Teste", 4.50)

produtoDao.cadastrar_produto(produto)
resultado = produtoDao.listar_produtos()
print(resultado)