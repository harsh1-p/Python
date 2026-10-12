#Convert python file into json 


import json

student_data = {
    "Name" : "Harsh Laxman Patil",
    "Cgpa" : 8.92
}

with open ("Student.json","w") as newfile:
    json.dump(student_data,newfile,indent=2)

print("Done")