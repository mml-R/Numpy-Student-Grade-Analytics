import numpy as np


student_type = np.dtype([('id',int),('age',int),
                         ('math',float),('physics',float),('english',float),('avg',float)])


AVAILABEL_COURSES = ["math","physics","english","avg"]

def generate_array(length):


    """
    Generate a structured array containing random student records.

    Parameters
    ----------
    length : int
        Number of students.

    Returns
    -------
    numpy.ndarray
        Structured array of students.
    """


    students = np.zeros(length,dtype=student_type)
    students['id'] = np.arange(length)
    students['age'] = np.random.randint(10,18,length)
    students['math'] = np.random.uniform(1,20,length)
    students['physics'] = np.random.uniform(1,20,length)
    students['english'] = np.random.uniform(1,20,length)
    students['avg'] = (students['math']+students['physics']+students['english'])/3
    return students
