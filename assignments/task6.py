#create a dictionary with 3 students and their marks. print all names and their marks.
student = {
    "student1":{
        "name":"kroman bhandari",
        "marks":{
            "english":40,
            "physics":45,
            "chemistry":50,
            "math":40,
            "nepali":40
        }
    },
    "student2":{
        "name":"samir rasaili",
        "marks":{
            "english":50,
            "physics":55,
            "chemistry":60,
            "math":60,
            "nepali":60
        }

    },
"student3":{
        "name":"lalu parsad rajbansi",
        "marks":{
            "english":60,
            "physics":50,
            "chemistry":55,
            "math":50,
            "nepali":60
        }
    }
}
# Print all names and their marks
for key,value in student.items():
    print(key)
    print("Name:",value["name"])
    print("Marks:")
    for subject,mark in value["marks"].items():
        print(f"  {subject.capitalize()} : {mark}")
    print("\n")