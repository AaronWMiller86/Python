class Dog:
    def __init__(self, name, breed, age, weight):
        self.name = name
        self.breed = breed
        self.age = age
        self.weight = weight


    def walk_dog(self, time):
         print("You walk " + self.name + " the " + str(self.age) + " year old " + self.breed + " for " + str(time) + " minutes.")


    def feed_dog(self, bag_weight, bag_cost):
        price = (bag_cost / (bag_weight * 4))
        fd = {
            12 : 1,
            20 : 1.3,
            35 : 2,
            50 : 2.6,
            75 : 3.3,
            100: 4.25        
        }
        amount = 0
        if self.weight > 100:
            amount = 4.25 + (((self.weight - 100) / 10 ) * .25)
        else:
            for i in fd:
                if self.weight <= i:
                    amount = fd[i]
                    break
        
        print("Feed " + self.name + " " + "{:.3f}".format(amount) + " cups of food. It will cost $" + "{:.2f}".format(amount * price))
   

d1 = Dog("Sugar Bear", "Boxer Mix", 12, 45)
d2 = Dog("Sunny", "Beagle", 13, 20)
d3 = Dog("Big Boi", "Husky", 3, 125)

d1.feed_dog(16.5, 35.10)
d2.feed_dog(16.5, 35.10)
d3.feed_dog(16.5, 35.10)
