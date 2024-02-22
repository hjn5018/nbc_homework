class Monster():
    hp = 100
    alive = True
    
    def damage(self, attack):
        self.hp = self.hp - attack
        # if self.hp < 100:
        #     alive = False
        # else:
        #     alive = True

    def check_status(self):
        if self.hp > 0:
            print(self.hp)
        else:
            print("Died")

monster1 = Monster()
monster2 = Monster()

monster1.damage(100) # AttributeError: 'NoneType' object has no attribute 'damage'
monster1.check_status()
monster2.damage(65)
monster2.check_status()