#1
grades = {
    "Math": 80,
    "Physics": 90,
    "Chemistry": 85
}
print(grades)

for i in grades.keys():
    print(i)


#2
grades = {
    "Math": 80,
    "Physics": 90,
    "Chemistry": 85
}
print(grades)

x = grades.values()
print(x)

a = sum(x)
print(a)


#3
grades = {"Math": 80, "Physics": 90, "Chemistry": 85}
print(grades)

for v, k in grades.items():
    if k > 85:
        print(v, k, "Excellent")
    else:
        print(v, k)


#4
inventory = {
    "pen": 10,
    "pencil": 20,
    "notebook": 15
}
print(inventory)

c = inventory.get("eraser", 0)
print(c)


#5
scores = {
    "Ali": 85,
    "Vali": 90,
    "Hasan": 78
}
print(scores)

for a, b in scores.items():
    print(f"{a} scored {b} points")
