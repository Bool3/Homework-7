import csv

db = {}

def _format(x):
    if x == '':
        return None
    else:
        return float(x)

with open("song_db_01.csv", "r") as file:
    rawdata = csv.DictReader(file)
    
    adv_topics_students_data = [row for row in rawdata if row['Adv Topics'] == 'y']

    assert len(adv_topics_students_data) == 11
    #print(adv_topics_students_data[0])

    for student_data in adv_topics_students_data:
        db[student_data['PKID']] = {k: _format(v) for k,v in student_data.items() if k not in ['Adv Topics', 'PKID']}


ids = ['student1397', 'student1890', 'student4157', 'student4917', 'student5231', 'student632', 'student7408', 'student914', 'student9279', 'student9550', 'student9804']

assert len(db) == 11
assert all( id in ids for id in db.keys())

def shared(student_a, student_b):
    sid_a = 'student' + student_a
    sid_b = 'student' + student_b

    a = set(song for song in db[sid_a] if db[sid_a][song] != None)
    b = set(song for song in db[sid_b] if db[sid_a][song] != None)

    shared = a.intersection(b)

    return shared

def euclidean(dictionary_key_studentId_value_ratings, studentId_1, studentId_2):
    pass