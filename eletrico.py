class Pikachu:
  
  def __init__(self, __treinador):
    print("novo lutador")
    self.__hp = 100
    self.__mp = 100
    self.__treinador = __treinador
  
  def showStatus(self):
      print("\n Pikachu de {} \n __hp = {} \n __mp = {}".format(self.__treinador, self.__hp, self.__mp))
  
  def choqueDoTrovao(self, pokemon):
    print("\n {} diz: pikachu! choque do trovão!".format(self.__treinador))
    self.__mp = self.__mp - 15
    pokemon.receberDano(35)
  
  def caudaDeFerro(self, pokemon):
    print("\n {} diz: pikachu! cauda de ferro nele!".format(self.__treinador))
    self.__mp = self.__mp - 5
    pokemon.receberDano(15)
  
  def investidaDoTrovao(self, pokemon):
    print("\n {} diz: pikachu! investida do trovão!".format(self.__treinador))
    self.__mp = self.__mp - 5
    self.__hp = self.__hp - 3
    pokemon.receberDano(30)
  
  def receberDano(self, valorDoDano):
    self.__setHP((self.getHP()-valorDoDano))
    print("pikachu de {} recebe {} de dano".format(self.__treinador, valorDoDano))
    if ((self.getHP()-valorDoDano)) <= 0:
      print("pikachu de {} esta fora de combate.".format(self.__treinador))
  
  def getHP(self):
    return self.__hp
    
  def getMP(self):
    return self.__mp
    
  def __setHP(self, novoHP):
    self.__hp = novoHP
  
  def __setMP (self, novoMP):
    self.__mp = novoMP
    
  