student={
    "student1":{
        "name":"kroman bhandari",
        "marks":60
        },
    "student2":{
        "name":"samir rasaili", 
        "marks":70
        },  
    "student3":{
        "name":"lalu parsad rajbansi",  
        "marks":80
        }
}
top_mark=-1
top_name=""
for key, value in student.items():
    if value["marks"]>top_mark:
        top_mark = value["marks"]
        top_name = value["name"]
print(f"{top_name} has hightest marks:{top_mark}")        
