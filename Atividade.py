class Familia:
    __nome = None
    __identidade = None
    __situacao = "Solteiro"

    def __init__(self,nome):
        self.__nome = nome

    def Casar(self,x):
        self.__situacao = "Casado"
        print(self.__nome,"casou-se com",x)

    def getNome(self):
        return self.__nome

    def setNome(self,nome):
        self.__nome = nome

    def getIdentidade(self):
        return self.__identidade

    def setIdentidade(self,identidade):
        self.__identidade = identidade

    def Identificar(self,y):
        print(self.__nome,"é",self.__identidade,"de",y)

    def Nascer(self,x,y):
        print(self.__nome,"nasceu!")
        print(self.__nome,"é filho(a) de",x,"e de",y)


