from typing import Type
from model.produto import Produto
from model.connection import Connection

class ProdutoDAO:

    def __init__(self) -> None:
        self.__conn = None

    def cadastrar_produto(self, produto: Type[Produto]) -> None:
        self.__conn = Connection().get_Connection()
        cursor = self.__conn.cursor()
        comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{produto.get_nome_produto()}", {produto.get_valor_produto()})'
        cursor.execute(comando)
        self.__conn.commit() # edita o banco de dados
        cursor.close()
        self.__conn.close()

    def listar_produtos(self) -> Type[list]:
        self.__conn = Connection().get_Connection()
        cursor = self.__conn.cursor()
        comando = "SELECT * FROM vendas"
        cursor.execute(comando)
        resultado = cursor.fetchall() # ler banco de dados
        cursor.close()
        self.__conn.close()
        return resultado
        
    def deletar_produto(self, produto: Type[Produto]) -> None:
        self.__conn = Connection().get_Connection()
        cursor = self.__conn.cursor()
        comando = f'DELETE FROM vendas WHERE idVendas="{produto.get_id_produto()}"'
        cursor.execute(comando)
        self.__conn.commit()
        cursor.close()
        self.__conn.close()

    def alterar_produto(self, produto: Type[Produto]):
        self.__conn = Connection().get_Connection()
        cursor = self.__conn.cursor()
        comando = f'''UPDATE vendas SET nome_produto=
        "{produto.get_nome_produto()}", 
        valor={produto.get_valor_produto()} 
        WHERE idVendas={produto.get_id_produto()}'''
        cursor.execute(comando)
        self.__conn.commit()
        cursor.close()
        self.__conn.close()


