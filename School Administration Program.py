#Write a program that can be used for school administration 
import csv

def write_file(list_): #Writing a function to convert info to csv file 
    with open('Studentinfo.csv','a',newline='') as Student_file: #Creating a new file
        writer= csv.writer(Student_file) #Creating a writer 
        
        
        if Student_file.tell()==0: #So that labels are written only once 
            writer.writerow(['Name','Last_Name', 'Age', "Contact_Number", 'E-Mail_ID'])
        writer.writerow(list_)
        
if __name__=='__main__':
    
    condition=True
    studentcount=1
    while condition:
        studentinfo=input(f'Enter the information for #{studentcount}in the following format (Name LastName Age Contact_Number E-Mail_ID)')
        
        splittedinfo=studentinfo.split()
        print(f'You have entered\n Name: {splittedinfo[0]}\n Last Name: {splittedinfo[1]}\n Age: {splittedinfo[2]}\n Contact_Number: {splittedinfo[3]}\n E-Mail_ID: {splittedinfo[4]}')
        choice=input('Are you satisfied with your input(yes/no)') #Checking if the entered info is correct 
        
        if choice=='yes' or 'Yes':
            write_file(splittedinfo)
            
            choice1=input('Do you want to enter for another student? (yes/no)') #Checking if another entry is to be made
            
            if choice1=='yes' :
                condition=True
                studentcount+=1
            elif choice1=='no' :
                condition=False
        elif choice== 'no' :
            print('Please enter the information again')  #Asking the user to re enter the values 
        
    
     


