import random 

class Character:
  def __init__(self, name, health, level):
    self.__name = name
    self.__health = health
    self.__level = level

  def get_name(self):
    return self.__name

  def get_health(self):
    return self.__health

  def get_level(self):
    return self.__level
  
  def show_details(self):
    return f"Name: {self.get_name()}\nHealth: {self.get_health()}\nLevel: {self.get_level()}"
  
  def receive_attack(self, damage):
    self.__health -= damage
    if self.__health < 0:
      self.__health = 0  

  def attack(self, target):
    damage = random.randint(self.get_level() * 2, self.get_level() * 4)
    target.receive_attack(damage)
    print(f"{self.get_name()} attacked the {target.get_name()} and dealt {damage} damage!")
  
class Hero(Character):
  def __init__(self, name, health, level, skill):
    super().__init__(name, health, level)
    self.__skill = skill

  def get_skill(self):
    return self.__skill
  
  def show_details(self):
    return f"{super().show_details()}\nSkill: {self.get_skill()}\n"
  
  def special_skill(self, target):
    damage = random.randint(self.get_level() * 1, self.get_level() * 6)
    target.receive_attack(damage)
    print(f"{self.get_name()} used the special skill {self.get_skill()} in the {target.get_name()} and dealt {damage} damage!")
  
class Enemy(Character):
  def __init__(self, name, health, level, type):
    super().__init__(name, health, level)
    self.__type = type
  
  def get_type(self):
    return self.__type
  
  def show_details(self):
    return f"{super().show_details()}\nType: {self.get_type()}\n"

class Game:
  """class responsible for the logic and orchestration of the game"""
  
  def __init__(self) -> None:
    self.hero = Hero("Hero", 100, 5, "Fire Ball")
    self.enemy = Enemy("Snake", 80, 6, "Venomous")

  def start_battle(self):
    """management of turn-based battles"""
    print("Starting the battle!")
    while self.hero.get_health() > 0 and self.enemy.get_health()>0:
      print("\nCharacters Details:")
      print(self.hero.show_details())
      print(self.enemy.show_details())

      input("Press Enter to attack...")
      choice = input("Choose (1- Normal Attack, 2- Special Skill): ")

      if choice == '1':
        self.hero.attack(self.enemy)
      elif choice == '2':
        self.hero.special_skill(self.enemy)
      else:
        print("Invalid choice. Choose again...")

      if self.enemy.get_health() > 0:
        self.enemy.attack(self.hero)
    
    if self.hero.get_health() > 0:
      print("\nCongratulations you won the battle!\n")
    else:
      print("\nYou lost the battle! Wish you luck in your next adventure\n")

# Game Instance
game = Game()
game.start_battle()