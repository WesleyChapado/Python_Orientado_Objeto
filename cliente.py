class Cliente:
    def __init__(self, nome):
        self.__nome = nome

    #vincula o metodo com o construtor "nome"
    @property
    def nome(self):
        return self.__nome.title()

    #cria um set para o construtor "nome"
    @nome.setter
    def nome(self, nome):
        self.__nome  = nome