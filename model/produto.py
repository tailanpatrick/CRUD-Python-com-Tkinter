class Produto:

    def __init__(self, nome_produto: str, valor_produto: float) -> None:
        self.__id_produto = None
        self.__nome_produto = nome_produto
        self.__valor_produto = valor_produto

    def get_id_produto(self) -> int:
        return self.__id_produto
    
    def get_nome_produto(self) -> str:
        return self.__nome_produto
    
    def get_valor_produto(self) -> float:
        return self.__valor_produto
    
    def set_id_produto(self, id: str) -> None:
        self.__id_produto = id
       
    def set_nome_produto(self, nome: str) -> None:
        self.__nome_produto = nome
    
    def set_valor_produto(self, valor: float) -> None:
        self.__valor_produto = valor

    
