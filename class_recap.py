class Monster():
    hp = 100
    alive = True
    
    def damage(self, hp):
        self.hp = self.hp - hp
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

monster1.damage(10) # AttributeError: 'NoneType' object has no attribute 'damage'
monster1.check_status()