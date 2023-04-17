import uuid
class Guest:
    def __init__(self,name,age,cash,fav_song,fav_genre):
        self.id = uuid.uuid4
        #UUID (Universally Unique Identifier)
        # Time-based (version 1)
        # DCE Security (version 2)
        # Name-based (version 3 and 5)
        # Random (version 4)
        self.name = name
        self.cash = cash
        self.age = age
        self.favorite_song = fav_song
        self.favorite_genre = fav_genre
        
    def guest_pay(self,amount):
        if self.cash >= amount:
            self.cash -= amount
        else:
            return "Can't afford"

    def can_afford(self,value):
        return self.cash >= value
    

    

    # def guest_match(self,other_guest):
    #     if (self.name == other_guest.name and
    #         self.age == other_guest.age and
    #         self.favorite_song == other_guest.favorite_song and
    #         self.favorite_genre == other_guest.favorite_genre):
    #         return True
    #     return False