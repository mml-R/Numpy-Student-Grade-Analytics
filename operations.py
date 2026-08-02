import numpy as np
from generator import *

def show_top_ten(array):

    """
    Display the top 10 students sorted by average score.
    """

    array = array[array['avg'].argsort()][::-1]
    print("ID   AGE    AVG")
    print("-"*30)
    for i in range(min(10,len(array))):
        print(f"{array[i]['id']}   {array[i]['age']}   {array[i]['avg']:.2f}")


def show_bottom_ten(array):

    """
    Display the bottom 10 students sorted by average score.
    """

    array = array[array['avg'].argsort()]
    print("ID   AGE    AVG")
    for i in range(min(10,len(array))):
        if array[i]['avg'] > 0:
            print(f"{array[i]['id']}   {array[i]['age']}   {array[i]['avg']:.2f}")




def remove_below_mean(array):

    """
    Remove all students whose average score is below the class average.

    Returns
    -------
    numpy.ndarray
    Filtered student array.
    """

    mask = array['avg'] < np.mean(array['avg'])
    return array[~mask] 
    


def avg_of_each_course(array,field):

    """
    Calculate the average score of a selected course.

    Parameters
    ----------
    field : str
    math, physics, english or avg.
    """

    return np.mean(array[field])



def sort_by_score(array,field):

    """
    Return students sorted in descending order by the selected field.
    """

    return array[array[field].argsort()][::-1]



def normalize_score(array,field='avg'):
    
    """
    Return the z-score normalization of the selected field.
    """

    normalized = (array[field] - np.mean(array[field])) / np.std(array[field])
    return normalized


def best_student(array,field):

    """
    Return the student with the highest value in the selected field.
    """

    return array[array[field].argmax()]


def worst_student(array,field):

    """
    Return the student with the lowest value in the selected field.
    """

    return array[array[field].argmin()]


def search_by_id(array,id):

    """
    Search a student by ID.

    Returns
    -------
    numpy.void or None
        Student record if found, otherwise None.
    """

    mask = array['id'] == id
    
    if np.any(mask):
        return array[mask][0]

    return None


def print_student(look_for):  

    """
    Print a formatted summary of a student's information.
    """

    print("=" * 35)
    print(f"ID      : {look_for['id']}")
    print(f"Age     : {look_for['age']}")
    print(f"Math    : {look_for['math']:.2f}")
    print(f"Physics : {look_for['physics']:.2f}")
    print(f"English : {look_for['english']:.2f}")
    print(f"Average : {look_for['avg']:.2f}")
    print("=" * 35)


def get_int(prompt):

    """
    Prompt the user until a valid integer is entered.
    """

    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.") 

