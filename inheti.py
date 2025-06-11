# class Animal:
#     def __init__(self,state,city):
#         self.state=state
#         self.city=city

#     def __str__(self):
#         return "The instance of the class has some return value"
    
#     def sound():
#         print("Make a sound")

# animal=Animal("telangana","Hyderabad")
# print(animal)

# class dog(Animal):
#     def __init__(self, state, city):
#         super().__init__(state,city)

#     def sound(self):
#         return"wuff wuff"
        

# bruno=dog("dfd","fdfd")
# print(bruno.state)
# print(bruno.city)

# print(bruno.sound())


# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort(key=str.upper,reverse=True)
# print(thislist)


my_array = [7, 12, 9, 4, 11, 8]
min_value = my_array[0]


for x in my_array:  
    if x<min_value:
        min_value=x

print(min_value)
