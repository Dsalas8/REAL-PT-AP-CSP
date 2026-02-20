#This program is trying to calculate the grades of people in a variety of subjects, showing the lowest grade and the highest grade. 

print("Hello and welcome to GPATRACKER! The place where managing and viewing grades is easier than ever. Whenever you're ready, lets get started!")
def function_1():
    Math = [89, 100, 95, 93, 89]                                            #VALUES FOR MATH 
    English = [99, 100, 88, 85, 91]                                         #VALUES FOR ENGLISH
    Science = [83, 82, 100, 95, 82]                                         #VALUES FOR SCIENCE
    Social_Studies = [100, 94, 88, 90, 92]                                  #VALUES FOR SOCIAL STUDIES
    ask = print("Would you like to any grades to a specific class? ")
    if ask == "yes":
        Region = input("Enter the class in which youd like to add a grade: ")
        if Region == "Math":
            new = input("Enter your new grade: ")
            Math.insert(-1,new)
        elif Region == "English":
            new = input("Enter your new grade: ")
            English.insert(-1,new)
        elif Region == "Social Studies":
            new = input("Enter your new grade: ")
            Social_Studies.insert(-1,new)
        elif Region == "Science":
            new = input("Enter your new grade: ")
            Science.insert(-1,new)
        
        
    if ask == "no":
        response = input("Would you like to review your grades once more? ")
        if response == "Yes":
            function(2)
        if response == "no":
            print("Have a Great Day!")
            print("--------------------------")
def function_2():
    print("Select the class you'd like to view")
    Math = [89, 100, 95, 93, 89]                                            #VALUES FOR MATH 
    English = [99, 100, 88, 85, 91]                                         #VALUES FOR ENGLISH
    Science = [83, 82, 100, 95, 82]                                         #VALUES FOR SCIENCE
    Social_Studies = [100, 94, 88, 90, 92]                                  #VALUES FOR SOCIAL STUDIES
    classes = ["Math: 93.2%", "English: 92.6%", "Science: 88.4%", "Social Studies: 92.8%"]          #THE LIST HAS SUBJECTS WITH CERTAIN GRADE VALUES, AND WILL BE EXTRACTED WHEN ASKING WHAT CLASS WILL BE VIEWED
    print("[Math, English, Science, Social Studies]")
    subject = input("Enter the class youd like to view: ")
    print("You chose " + subject + ", Here is your grade!")
    if subject == "Math":
        print(classes[0])
        print("Here below are your recent grades for " + subject +":")
        print(Math[0:])
    if subject == "English":
        print(classes[1])
        print("Here below are your recent grades for " + subject +":")
        print(English[0:])
    if subject == "Science":
        print(classes[2])
        print("Here below are your recent grades for " + subject +":")
        print(Science[0:])
    if subject == "Social Studies":
        print(classes[3])
        print("Here below are your recent grades for " + subject +":")
        print(Social_Studies[0:])
    retry = input("Do you want to look at other classes grades? ")
    while retry == "yes":
        print("Ok, here we go again.")
        print("--------------------------")
        function_2() 
    if retry == "no":
        print("Ok, Have a great day!")
        function_1()
        return                                                          
print("----------------------------")
function_2()



#CREATE A FUNCTION FOR THE WHOLE CODE 


