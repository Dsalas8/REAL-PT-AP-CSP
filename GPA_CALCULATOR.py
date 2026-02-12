#This program is trying to calculate the grades of people in a variety of subjects, showing the lowest grade and the highest grade. 
print("Hello and welcome to GPATRACKER! The place where managing and viewing grades is easier than ever. Whenever you're ready, lets get started!")
print("Select the class you'd like to view")
Math = [89, 100, 95, 93, 89]
English = [99, 100, 88, 85, 91]
Science = [83, 82, 100, 95, 82]
Social_Studies = [100, 94, 88, 90, 92]
classes = ["Math: 93.2%", "English: 92.6%", "Science: 88.4%", "Social Studies: 92.8%"]

print("[Math, English, Science, Social Studies]")
subject = input("Enter the class youd like to view: ")

print("You chose " + subject + ", Here is your grade!")
if subject == "Math":
    print(classes[0])
    print("Here below are your recent grades for" subject)
    print(Math[0:])

