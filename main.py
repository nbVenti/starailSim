



class Simulation():
    def __init__(self):
        self.characters = []
        self.action_value = 0

    def add_character(self, character):
        self.characters.append(character)

    def next_turn(self):
        self.turn += 1
        for character in self.characters:
            character.next_turn()






class Character():
    def __init__(self, name, element, health, attack, speed, dmg_multiplier, break_effect):
        self.name = name
        self.element = element
        self.health = health
        self.attack = attack
        self.speed = speed
        self.dmg_multiplier = dmg_multiplier
        self.break_effect = break_effect
        
    

            
            
        
   