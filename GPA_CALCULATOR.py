#This program is trying to calculate the grades of people in a variety of subjects, showing the lowest grade and the highest grade. 

print("Hello and welcome to GPATRACKER! The place where managing and viewing grades is easier than ever. Whenever you're ready, lets get started!")
def function_1():
    Math = [89, 100, 95, 93, 89]                                            #VALUES FOR MATH 
    English = [99, 100, 88, 85, 91]                                         #VALUES FOR ENGLISH
    Science = [83, 82, 100, 95, 82]                                         #VALUES FOR SCIENCE
    Social_Studies = [100, 94, 88, 90, 92]                                  #VALUES FOR SOCIAL STUDIES
    print("-----------------------")
    ask = input("Would you like to add any grades to a specific class? ")  #ASKS FOR WHAT CLASS THEY WANT TO REVIEW GRADES 
    if ask == "yes":
        Region = input("Enter the class in which youd like to add a grade: ") #ASKS FOR CLASS INPUT
        if Region == "Math":
            new = int(input("Enter your new grade: "))  #FOR EVERY "elif" ASKS FOR NEW GRADE INPUT, PRINTS NEWLY CHANGED LIST
            Math.append(new)
            print("Here are your updated grades!")
            print(Math)
            total_sum = sum(Math)   #The following counts the sum of the integers in the modified lists, and calculates the average for the new grade.
            count = len(Math)
            AVERAGE = round(total_sum/count, 2)
            print(f"Your new Grade Average is:{AVERAGE}%")
            print("Redirecting to start...")  #Commentary to redirect user so they know whats happening
        elif Region == "English":
            new = int(input("Enter your new grade: "))
            English.append(new)
            print("Here are your updated grades!")
            print(English)
            total_sum = sum(English)        #The following counts the sum of the integers in the modified lists, and calculates the average for the new grade.
            count = len(English)
            AVERAGE = round(total_sum/count, 2)
            print(f"Your new Grade Average is:{AVERAGE}%")
            print("Redirecting to start...") #Commentary to redirect user so they know whats happening
        elif Region == "Social Studies":
            new = int(input("Enter your new grade: "))
            Social_Studies.append(new)
            print("Here are your updated grades!")
            print(Social_Studies)
            total_sum = sum(Social_Studies)  #The following counts the sum of the integers in the modified lists, and calculates the average for the new grade.
            count = len(Social_Studies)
            AVERAGE = round(total_sum/count, 2)
            print(f"Your new Grade Average is:{AVERAGE}%")
            print("Redirecting to start...")           #Commentary to redirect user so they know whats happening
        elif Region == "Science":
            new = int(input("Enter your new grade: "))
            Science.append(new)
            print("Here are your updated grades!")
            print(Science)            
            total_sum = sum(Science)        #The following counts the sum of the integers in the modified lists, and calculates the average for the new grade.
            count = len(Science)
            AVERAGE = round(total_sum/count, 2)
            print(f"Your new Grade Average is:{AVERAGE}%")
            print("Redirecting to start...")    #Commentary to redirect user so they know whats happening 

    if ask == "no":             #If they answer no....
        function_3()            #Goes to function 3 which will ask if they want to finalize review on anything.

def function_2():           #Purpose is to ask what classes theyd like to view.
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
    print("----------------------")
    retry = input("Do you want to look at other classes grades? ")
    while retry == "yes":
        print("Ok, here we go again.")
        print("--------------------------")
        function_2() 
        if retry == "no":
         break
    function_1()

def function_3():
    print("-----------------------------")
    answer = input("Would you like to review your grades once more? ")  #Give user last chance to view grades.
    if answer == "yes":
        print("---------------------------")
        function_2()  #If yes, directs them back to function where the block of code is repeated.
    import sys                          
    if answer == "no":
        print("Have a good day!")
        sys.exit()                     #Ends program from any function.
     
         
    
                                                         
print("----------------------------")
function_2()



#CREATE A FUNCTION FOR THE WHOLE CODE 


