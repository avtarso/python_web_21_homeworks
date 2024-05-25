"""
running a set of different queries
"""

from functions import get_session
from settings import DATABASE
import selects


def main():

    ERROR = "Error. You must enter a valid number."
    VALUE_RANGE = f"The range of acceptable values is between 1 and 12 or 0"
    INPUT = '''Here yoou can get answers to the following queries:
1 - Find the 5 students with the highest average score in all subjects
2 - Find the student with the highest average score in a certain subject
3 - Find the average score in groups for a certain subject
4 - Find the average score on the stream (over the entire score table)
5 - Find which courses a certain teacher teaches
6 - Find a list of students in a certain group
7 - Find the grades of students in a separate group on a certain subject
8 - Find the average score given by a certain teacher in his subjects
9 - Find the list of courses attended by the student
10 - A list of courses taught to a particular student by a particular teacher
11 - The average score given by a certain teacher to a certain student
12 - Grades of students in a certain group on a certain subject in the last lesson
0 - Exit
Please, input your choice --->>'''
    
    selected_func = {
        1: selects.select_1,
        2: selects.select_2,
        3: selects.select_3,
        4: selects.select_4,
        5: selects.select_5,
        6: selects.select_6,
        7: selects.select_7,
        8: selects.select_8,
        9: selects.select_9,
        10: selects.select_10,
        11: selects.select_11,
        12: selects.select_12
    }

    while True:
        
        while True:

            try:
                choiced_select = int(input(INPUT))

                if choiced_select == 0:
                    print("Exiting the program. Goodbye!")
                    quit()

                if choiced_select in selected_func or choiced_select == 0:
                    break
                else:
                    print(VALUE_RANGE)

            except ValueError:
                print(ERROR)

        with get_session(DATABASE) as session:
            results, name_select = selected_func[choiced_select](session)

        BORDER = '#--------------------------------------------------------------------------------#'
        print(BORDER)
        print(name_select)
        print(BORDER)
        for result in results:
            print(result)
        print(BORDER)
        print("")


if __name__ == '__main__':
    main()