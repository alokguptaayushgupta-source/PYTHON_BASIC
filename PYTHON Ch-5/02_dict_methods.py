d = {}  # is a empty dect
marks = {
"Alok":100,
"Ananya":98,
"Arya":99,
"Ayush":100,
"sumit":55,
100:"alok"
}
print(marks.items())

print(marks.keys())

print(marks.values())

marks.update({"Ananya": 99,"ananya": 99})

print(marks)


print(marks.get("Alok1")) # Print None

# print(marks["Alok1"]) # Return an error

print(len(marks))