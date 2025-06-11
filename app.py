
class available:
    
    name="satish"
    age=26
    print("this is inside available")
    val=4**3
    def __init__(self):
        self.name="rahul"
        self.age=34
        self.trainagle=90

    newAttr={
        "horse":"Thoroughbreed",
        "matchesWon":90

    }

print(available.name)
check=available()
print(check.name)
print(check.val)
print(check.trainagle)
# this is the next part of learning
print(check.newAttr["horse"])
print(check.newAttr["matchesWon"])