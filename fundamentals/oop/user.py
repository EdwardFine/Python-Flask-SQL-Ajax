class user:
    def __init__(self,first_name,last_name, email, age, is_rewards_member=False,gold_card_points=0):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = is_rewards_member
        self.gold_card_points = gold_card_points
        
    def display_info(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Is rewards member: {self.is_rewards_member}")
        print(f"Gold Card Points: {self.gold_card_points}")
    def enroll(self):
        if self.is_rewards_member:
            print("User already a member")
        else:
            self.is_rewards_member=True
            self.gold_card_points +=200
    def spend_points(self, amount):
        if self.gold_card_points < amount:
            print(f"Insufficient Funds. Cannot make a purchase of {amount} points with a balance of {self.gold_card_points} points")
            
        else:
            self.gold_card_points -= amount
            print(f"New Gold Card Points Balance: {self.gold_card_points}")



samantha = user("Samantha","Maxis","samanthamaxis@gmail.com","10")
samantha.display_info()
samantha.enroll()

edward = user("Edward","Richtofen","group935@yahoo.com","34",True,5000)
tank = user("Tank","Dempsey","america4life@outlook.com","36",True,25)

samantha.spend_points(50)

edward.enroll()

edward.spend_points(80)

samantha.display_info()
edward.display_info()
tank.display_info()

samantha.enroll()

tank.spend_points(40)