import numpy as np
from generator import *
from operations import *

np.set_printoptions(precision=2)
while True:
    main_page = input("1-Generate array 2-Exit: ")
    match main_page:
        case "1":
            length = get_int("Enter the size of the array: ")
            students = generate_array(length)
            print(f"Created an array with {length} students.")

            while True:
                menu = input("1-Show array 2-Show top ten 3-Show bottom ten 4-Remove below average\n5-Average of each course 6-Sort by score 7-Normalize score 8-Find best student 9-Find worst student 10-Search by ID 11-Exit :")
                match menu:
                    case "1":
                        print(students)

                    case "2":
                        show_top_ten(students)

                    case "3":
                        show_bottom_ten(students)

                    case "4":
                        students = remove_below_mean(students)
                        print(students)

                    case "5":
                        course_name = input("Enter the name of the course(math,physics,english,avg): ")
                        if course_name.lower() in AVAILABLE_COURSES:
                            print(f"{avg_of_each_course(students,course_name):.2f}")
                        else:
                            print("Invalid input.\nAvailable courses: math , physics , english , avg")
                        
                    case "6":
                        course_name = input("Enter the name of the course(math,physics,english,avg): ")
                        if course_name.lower() in  AVAILABLE_COURSES:
                            print(sort_by_score(students,course_name))
                        else:
                            print("Invalid input.\nAvailable courses: math , physics , english , avg")

                    case "7":
                        course_name = input("Enter the name of the course(math,physics,english,avg): ")
                        if course_name.lower() in  AVAILABLE_COURSES:
                            print(normalize_score(students,course_name))
                        else:
                            print("Invalid input.\nAvailable courses: math , physics , english , avg")

                    case "8":
                        course_name = input("Enter the name of the course(math,physics,english,avg): ")
                        if course_name.lower() in  AVAILABLE_COURSES:
                            found = best_student(students,course_name)
                            print_student(found)
                        else:
                            print("Invalid input.\nAvailable courses: math , physics , english , avg")

                    case "9":
                        course_name = input("Enter the name of the course(math,physics,english,avg): ")
                        if course_name.lower() in  AVAILABLE_COURSES:
                            found = worst_student(students,course_name)
                            print_student(found)
                        else:
                            print("Invalid input.\nAvailable courses: math , physics , english , avg")

                    case "10":
                        student_id = get_int("Enter student ID: ")
                        found = search_by_id(students,student_id)

                        if found is None:
                            print("ID not found")
                            
                        else:
                            print_student(found)

                    case "11":
                        print("Closing...")
                        break


                    case _:
                        print("Invalid input!\nValid inputs: 1,2,3,4,5,6,7,8")
      


        
        case "2":
            print("Closing...")
            break

        case _:
            print("Please enter either 1 or 2.")
