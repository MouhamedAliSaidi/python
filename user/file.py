class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Rewards Member: {self.is_rewards_member}")
        print(f"Gold Card Points: {self.gold_card_points}")

    def enroll(self):
        if self.is_rewards_member:
            print("User already a member.")
            return False

        self.is_rewards_member = True
        self.gold_card_points = 200
        return True
            
    def spend_points(self, amount):
        if amount > self.gold_card_points:
            print("Insufficient points")
            return False

        self.gold_card_points -= amount
        return True

#3
user1 = User("John", "doe", "john.doe@gmail.com", 30)
user1.display_info()

#4
print("\nEnrolling user1:")
user1.enroll()
user1.display_info()

#5
user2 = User("Jane", "doe", "jane.d@gmail.com", 25)
user3 = User("Jorge", "doe'", "jorge.doe@gmail.com", 40)

#6 7
print("\nUser1 spends 50 points:")
user1.spend_points(50)
user1.display_info()

#8
print("\nEnrolling user2:")
user2.enroll()
user2.display_info()

#9
print("\nUser2 spends 80 points:")
user2.spend_points(80)
user2.display_info()

#10
print("\nDisplaying all users:")
user1.display_info()
print("------------------")
user2.display_info()
print("------------------")
user3.display_info()

#11
print("\nRe-enrolling user1:")
user1.enroll()
