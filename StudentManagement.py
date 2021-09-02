#Student management system

def calculate_highest_in_Maths(student_list):
    highest_score_in_Maths = 0
    highest_score_in_Maths_Name = ''
    from_the_city = ''
    for student in student_list:
        if (student.get("Maths") > highest_score_in_Maths):
            highest_score_in_Maths = student.get("Maths")
            highest_score_in_Maths_Name = student.get('name')
            highest_score_in_Maths_from_the_city = student.get('region')

    print(f"The highest scorer in Maths is {highest_score_in_Maths} by {highest_score_in_Maths_Name} from {highest_score_in_Maths_from_the_city}")

def calculate_highest_in_Science(student_list):
    highest_score_in_Science = 0
    highest_score_in_Science_Name = ''
    from_the_city = ''
    for student in student_list:
        if (student.get("Science") > highest_score_in_Science):
            highest_score_in_Science = student.get("Science")
            highest_score_in_Science_Name = student.get('name')
            highest_score_in_Science_from_the_city = student.get('region')

    print(f"The highest scorer in Science is {highest_score_in_Science} by {highest_score_in_Science_Name} from {highest_score_in_Science_from_the_city}")

student_1 = { "Maths" : 45,
              "Social" : 66,
              "Science" : 99,
              "name": "Bhargav",
              "region": "Bagepalli"
}

student_2 = { "Maths" : 75,
              "Social" : 86,
              "Science" : 79,
              "name": "Venkatesh",
              "region" : "Belgaum"
}

student_3 = { "Maths" : 85,
              "Social" : 96,
              "Science" : 87,
              "name": "Umesh",
              "region": "Udupi"
}

student_list = [student_1, student_2, student_3]
calculate_highest_in_Maths(student_list)
calculate_highest_in_Science(student_list)