import csv

test_db = {}

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
        test_db[student_data['PKID']] = {k: _format(v) for k,v in student_data.items() if k not in ['Adv Topics', 'PKID'] and k in ['Kiss', 'Scrubs', 'Space Cowboy', 'Pollyana', 'Moonlight Sonata', 'Young Dumb and Broke', 'Feeling Good']}


ids = ['student1397', 'student1890', 'student4157', 'student4917', 'student5231', 'student632', 'student7408', 'student914', 'student9279', 'student9550', 'student9804']

assert len(test_db) == 11
assert all( id in ids for id in test_db.keys())