print("Hello and welcome to GPATRACKER! The place where managing and viewing grades is easier than ever. Whenever you're ready, let's get started!")

def view():
    # Lists of grades
    Math = [89, 100, 95, 93, 89]
    English = [99, 100, 88, 85, 91]
    Science = [83, 82, 100, 95, 82]
    Social_Studies = [100, 94, 88, 90, 92]

    # List of class averages
    classes = ["Math: 93.2%", "English: 92.6%", "Science: 88.4%", "Social Studies: 92.8%"]

    while True:
        print("\nSelect the class you'd like to view:")
        print("[Math, English, Science, Social Studies]")

        subject = input("Enter the class you'd like to view: ")

        print("You chose " + subject + ", here is your grade!")

        if subject == "Math":
            print(classes[0])
            print("Recent grades:", Math)

        elif subject == "English":
            print(classes[1])
            print("Recent grades:", English)

        elif subject == "Science":
            print(classes[2])
            print("Recent grades:", Science)

        elif subject == "Social Studies":
            print(classes[3])
            print("Recent grades:", Social_Studies)

        else:
            print("That class does not exist. Try again.")
            continue

        retry = input("Do you want to look at another class? (yes/no): ")

        if retry.lower() == "no":
            print("Ok, have a great day!")
            break
        elif retry.lower() == "yes":
            print("Ok, here we go again.")
        else:
            print("Invalid response. Returning to menu.")
