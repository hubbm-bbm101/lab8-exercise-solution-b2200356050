import sys

student = {}

f=open(sys.argv[1], "r" , encoding="utf-8")

for line in f :
    name = line.split(":")[0]
    student[name]= (line.split(":")[1]).split(",")


for item in sys.argv[2].split(","):
    try:
        university = student[item][0]
        department = student[item][1]
        print("Name: " + str(item) + "university: " + str(university) + "department: " + str(department))

    except KeyError:
        print("\nno record of {} was found".format(item))
