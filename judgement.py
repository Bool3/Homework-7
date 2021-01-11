from extract_data import test_db

def shared(student_a, student_b, database=test_db):
    sid_a = 'student' + student_a
    sid_b = 'student' + student_b

    a = set(song for song in database[sid_a] if database[sid_a][song] != None)
    b = set(song for song in database[sid_b] if database[sid_a][song] != None)

    shared = a.intersection(b)

    return shared

def euclidean(dictionary_key_studentId_value_ratings, studentId_1, studentId_2):
    pass