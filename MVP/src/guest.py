class Guest:
    def __init__(self,name,cash,fav_song,fav_genre):
        self.name = name
        self.cash = cash
        
    def reduce_cash(self,amount):
        self.cash -= amount
