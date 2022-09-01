#Question 1
print("List of courses : ",'\n'"1. DM",'\n'"2. DSA",'\n'"3. EM-3",'\n'"4. LD",'\n'"5. MAL",'\n'"6. DSA LAB",'\n'"7. LD LAB",'\n'"8. MAL LAB")
def college():
    course_name = input("Enter the course (As given on the list) : ")
    sem = '3rd'
    credits = {'DM':'4','DSA':'3','EM-3':'4','LD':'3','MAL':'3','DSA LAB':'1','LD LAB':'1','MAL LAB':'1'}
    faculty_name = {'DM': 'Mr. Abhinav Singhal', 'DSA':'Ms. Pallavi R. Kumar', 'EM-3':'Dr. M. Shekar', 'LD': 'Mr. Deepak Varadan', 'MAL':'Mrs. P. Padma Priya Darshini', 'DSA LAB':'Ms. Pallavi R. Kumar','LD LAB': 'Mr. Deepak Varadan','MAL LAB':'Mrs. P. Padma Priya Darshini'}
    if course_name in credits : 
        print("Selected course : ",course_name)
        print("Credits : ",credits[course_name])
        print("Semester : ",sem)
        print("Faculty : ",faculty_name[course_name])
        CSE = ['DM','DSA','EM-3','LD','MAL','DSA LAB','LD LAB','MAL LAB'] 
        AIML = ['DM','DSA','EM-3','CC','MAA','MAA LAB','AI','ISP']
        if course_name in CSE and course_name in AIML:
            print("Course offered both in CSE and in AIML")
            return True
        else:
            print("Course not offered both in CSE and in AIML")
            return False        
    else:
        print("Invalid Input ", course_name, "is not present in this semester")
result = college() 
print(result)