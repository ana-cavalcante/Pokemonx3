from eletrico import Pikachu
p1 = Pikachu("Misty")
  
p2 = Pikachu("May")
  
p1.showStatus()
  
p2.showStatus()

p1.caudaDeFerro(p2)

p2.investidaDoTrovao(p1)

p1.showStatus()

p2.showStatus()

p1.choqueDoTrovao(p2)

p2.caudaDeFerro(p1)

p1.investidaDoTrovao(p2)

from fogo import Charmander

p3 = Charmander("may")

p3.flamethrower(p1)

