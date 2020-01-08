import pandas as pd
import random
import fpdf

#Set your desired team size here.
#If the number of students does not divide by this size,
#a team of this size plus one will be generated
initialTeamSize = 2

#initializes the output pdf
pdf = fpdf.FPDF(format='letter')
pdf.add_page()

#Change the font and size for the output PDF 
pdf.set_font("Arial", size=16)

#Reads the roster to a pandas data frame and constructs a list of the rows
#Change the name of this file to your csv containing student names
data = pd.read_csv("roster.csv")
lst = data.values.tolist()

#Generates a list of concatenated first and last names
classlist = []
for i in lst:
    classlist.append(str(i[0]+' '+i[1]))

#counts the number of students in the class    
students = len(classlist)

#sets the number of team    
teams = students//initialTeamSize

#Randomly samples the teams from the class list, removing selected students
#and decreasing the remaining number of teams.
while students > 0 and teams > 0:
    team = random.sample(classlist, int(students/teams))
    print(team)
    
    tmpcnt = 0
    teamsize = len(team)
    for x in team:
        tmpcnt +=1
        classlist.remove(x)
        pdf.write(10,str(x))
        if tmpcnt != teamsize:
            pdf.write(10," and ")
            
    pdf.ln()
    students -= int(students/teams)
    teams -= 1

#Outputs a PDF of the pairings, for easy projections    
pdf.output("teams.pdf")

