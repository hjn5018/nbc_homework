def Monster():
    hp = 100
    alive = True
    
    def damage(self, hp):
        self.hp = self.hp - hp
        if self.hp < 100:
            alive = False
        else:
            alive = True
        return self.hp

    def check_status():
        if alive == True:
            print("alive!")
        else:
            print("Died")

monster1 = Monster()
monster2 = Monster()

monster1.damage() # AttributeError: 'NoneType' object has no attribute 'damage'