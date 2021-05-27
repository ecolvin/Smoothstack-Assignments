#Three is a crowd
print("THREE IS A CROWD:")

def threeIsACrowd(lst):
    if len(lst) > 3:
        print("It\'s getting a little crowded in here...")

l = ["John", "Jacob", "Jingleheimer", "Schmidt"]
print(l)
threeIsACrowd(l)
l.remove(l[0])
l.remove(l[0])
print(l)
threeIsACrowd(l)
print("")
print("")
print("")

#Three is a crowd part 2
print("THREE IS A CROWD - PART 2:")

def threeIsACrowdPt2(lst):
    if len(lst) > 3:
        print("It\'s getting a little crowded in here...")
    else:
        print("This room is not very crowded!")

l = ["John", "Jacob", "Jingleheimer", "Schmidt"]
print(l)
threeIsACrowdPt2(l)
l.remove(l[0])
l.remove(l[0])
print(l)
threeIsACrowdPt2(l)
print("")
print("")
print("")

#Six is a Mob
print("SIX IS A MOB:")

def sixIsAMob(lst):
    if len(lst) > 5:
        print("What is this?! Some sort of flash mob?!?!")
    elif len(lst) > 2:
        print("It\'s getting a little crowded in here...")
    elif len(lst) > 0:
        print("This room is not very crowded!")
    else:
        print("Where\'d everybody go?")

l = ["John", "Jacob", "Jingleheimer", "Schmidt", "My", "Name", "Too"]
print(l)
sixIsAMob(l)
l.remove(l[0])
l.remove(l[0])
print(l)
sixIsAMob(l)
l.remove(l[0])
l.remove(l[0])
print(l)
sixIsAMob(l)
l.remove(l[0])
l.remove(l[0])
print(l)
sixIsAMob(l)
l.remove(l[0])
print(l)
sixIsAMob(l)
print("")
print("")
print("")