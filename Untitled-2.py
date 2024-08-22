class personagem:
   def __init__(self,name,life,attack):
      self.name = name
      self.life = life
      self.attack = attack
   
   def getWeapon(self):
      self.attack += 10
   
   def getArmor(self,raridade):
      self.life += (raridade * 10)

pessoa = personagem("Carlos",100,10)
pessoa.getWeapon()
pessoa.getArmor(10)
print(pessoa.attack)
print(pessoa.life)
