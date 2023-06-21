class Conta:
    def __init__(self,numero,saldo,titular):
        self.__numero = int(numero)
        self.__saldo = float(saldo)
        self.__titular = str(titular)
        
    
    def CriarConta()
       
        
    def get_numero(self):
        return self.__numero
        
    def set_numero(self,numero2):
        self.__numero = numero2
        
    def get_saldo(self):
        return self.__saldo
        
    def set_saldo(self, saldo2):
        self.__saldo = saldo2
        
    def get_titular(self):
        return self.__titular
        
    def set_titular(self, titular2):
        self.titular = titular2
        
    def mostrar_saldo(self):
        print(self.get_saldo())
        
    def depositar(self,valor: float):
        self.__saldo += valor
        
    def sacar(self,valor: float):
        self.__saldo -= valor
        
    def transferir(self):
        pass
