from extract_data import test_db
import math

def shared(studentID_a, studentID_b, database):
    db_stu_a = database[studentID_a]
    db_stu_b = database[studentID_b]

    a = set(song for song in db_stu_a if db_stu_a[song] != None)
    b = set(song for song in db_stu_b if db_stu_b[song] != None)

    shared = list(a.intersection(b))

    return shared

def euclidean(studentID_a, studentID_b, database):
    both_rated = shared(studentID_a, studentID_b, database)
    point_summation = 0

    for song in both_rated:
        point_summation += abs(database[studentID_a][song] - database[studentID_b][song]) ** 2
    
    return math.sqrt(point_summation)

assert math.isclose(euclidean('student914', 'student9804', test_db), 5.0)
assert math.isclose(euclidean('student5231', 'student4157', test_db), 3.0)
assert math.isclose(euclidean('student1397', 'student7408', test_db), 4.3589, rel_tol=0.0009)
