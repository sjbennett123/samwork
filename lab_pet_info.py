#!/bin/python3

class Pet:
    def __init__(self):
        self.name = ''
        self.age = 0

    def print_info(self):
        print('Pet Information:')
        print('   Name:', self.name)
        print('   Age:', self.age)

class Dog(Pet):
    def __init__(self):
        Pet.__init__(self) 
        self.breed = ''

    def print_info(self):
        print('Dog Information:')
        print('   Name:', self.name)
        print('   Age:', self.age)
  #      print('   Breed:', self.breed)

my_pet = Pet()
my_dog = Dog()
# pet_name = "sam" # input("pet_name: ")
# pet_age = 1 # int(input("pet_age: "))

dog_name = "scott" #input("dog_name: ")
dog_age = 45 # int(input("dog_age: "))
dog_breed = "marauder" # input("dog_breed: ")



# TODO: Create generic pet (using pet_name, pet_age) and then call print_info()
# my_pet.name = pet_name
# my_pet.age = pet_age
# Pet.print_info(my_pet)

# exit()

# TODO: Create dog pet (using dog_name, dog_age, dog_breed) and then call print_info()

my_dog.name = dog_name
my_dog.age = dog_age
my_dog.breed = dog_breed
Dog.print_info(my_dog)
# TODO: Use my_dog.breed to output the breed of the dog
print(my_dog.breed)

