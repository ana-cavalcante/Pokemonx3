class Charmander:
  
  def __init__(self, __treinador):
    print("novo lutador")
    self.__hp = 100
    self.__mp = 100
    self.__treinador = __treinador
  
  def showStatus(self):
      print("\n Charmander de {} \n __hp = {} \n __mp = {}".format(self.__treinador, self.__hp, self.__mp))
  
  def 	flamethrower(self, pokemon):
    print("\n {} diz: Charmander! choque do trovão!".format(self.__treinador))
    self.__mp = self.__mp - 15
    pokemon.receberDano(35)
  
  def  mordidaDoDragao(self, pokemon):
    print("\n {} diz: Charmander!  Morde ele!".format(self.__treinador))
    self.__mp = self.__mp - 5
    pokemon.receberDano(15)
  
  def 	flameBurst (self, pokemon):
    print("\n {} diz: Charmander! 	Flame Burst !".format(self.__treinador))
    self.__mp = self.__mp - 5
    self.__hp = self.__hp - 3
    pokemon.receberDano(30)
  
  def receberDano(self, valorDoDano):
    self.setHP((self.getHP()-valorDoDano))
    print("Charmander de {} recebe {} de dano".format(self.__treinador, valorDoDano))
    if ((self.getHP()-valorDoDano)) <= 0:
      print("Charmander de {} esta fora de combate.".format(self.__treinador))
  
  def getHP(self):
    return self.__hp
    
  def getMP(self):
    return self.__mp
    
  def setHP(self, novoHP):
    self.__hp = novoHP
  
  def setMP (self, novoMP):
    self.__mp = novoMP
    