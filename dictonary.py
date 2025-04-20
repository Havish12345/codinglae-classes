student_info= {
    "ID1":
    {"Name": "John",
    "Age": "20",
    "subject": "Computer Science",
    "Grade": "9",
    },
    "ID2":
    {"Name": "bob",
    "Age": "15",
    "subject": "history",
    "Grade": "7",
    },
      "ID3":
    {"Name": "Alice",
    "Age": "18",
    "subject": "Computer Science",
    "Grade": "9",
    },




    }
for student_id, student_details in student_info.items():
    print("student_id:", student_id)
    print("student_name:", student_details["Name"])
    print("student_age:", student_details["Age"])
    print("student_subject:", student_details["subject"])
    print("student_grade:", student_details["Grade"])
    print("-" * 30)


#print(student_info["ID1"])
#print(student_info["ID2"])

#x=student_info.values()
#print(x)