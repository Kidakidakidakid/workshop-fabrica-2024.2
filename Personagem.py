import random
class personagem:
   def __init__(self,name,life,attack):
      self.name = name
      self.life = life
      self.attack = attack
   
   def getWeapon(self):
      self.attack += 10
   
   def getArmor(self,raridade):
      self.life += (raridade * 10)
      
   def getHurt(self,raridade):
      self.life -= raridade * random.randint(1,3)

pessoa = personagem("Carlos",100,10)
pessoa.getWeapon()
pessoa.getArmor(10)
print(pessoa.attack)
print(pessoa.life)
