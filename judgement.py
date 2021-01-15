from extract_data import test_db
import math

def shared(studentID_a, studentID_b, database):
    db_stu_a = database[studentID_a]
    db_stu_b = database[studentID_b]

    a = set(song for song in db_stu_a if db_stu_a[song] != None)
    b = set(song for song in db_stu_b if db_stu_b[song] != None)

    shared = list(a.intersection(b))

    return shared

def sim_euclidean(studentID_a, studentID_b, database):
    both_rated = shared(studentID_a, studentID_b, database)
    point_summation = 0

    for song in both_rated:
        point_summation += abs(database[studentID_a][song] - database[studentID_b][song]) ** 2
    
    return math.sqrt(point_summation)
"""
print(sim_euclidean('student914', 'student9804', test_db))
assert math.isclose(sim_euclidean('student914', 'student9804', test_db), 0.0384, rel_tol = 0.009)
assert math.isclose(sim_euclidean('student5231', 'student4157', test_db), 0.1, rel_tol = 0.009) 
assert math.isclose(sim_euclidean('student1397', 'student7408', test_db), 0.05, rel_tol = 0.009)
"""
def sim_pearson(studentID_a, studentID_b, database):
    both_rated = shared(studentID_a, studentID_b, database)
    n = len(both_rated)

    sum_a = 0
    sum_b = 0
    sq_sum_a = 0
    sq_sum_b = 0
    sum_ab = 0

    for song in both_rated:
        sum_a += database[studentID_a][song]
        sum_b += database[studentID_b][song]
        sum_ab += database[studentID_a][song] * database[studentID_b][song]
        sq_sum_a += database[studentID_a][song] ** 2
        sq_sum_b += database[studentID_b][song] ** 2

    numerator = sum_ab - (sum_a * sum_b) / n

    denominator = math.sqrt((sq_sum_a - sum_a ** 2 / n) * (sq_sum_b - sum_b ** 2 / n))
    
    return numerator / denominator

assert math.isclose(sim_pearson('student914', 'student9804', test_db), 0.63246, rel_tol = 0.0009)
assert math.isclose(sim_pearson('student5231', 'student4157', test_db), -0.48038, rel_tol = 0.0009)
assert math.isclose(sim_pearson('student1397', 'student7408', test_db), -0.23338, rel_tol = 0.0009)

def top_matches(studentID, database, n=5, sim_function=sim_euclidean):
    matches = []
    
    def sort_by_sID(e):
        return e[1]

    for sID in database:
        if sID != studentID:
            matches.append((sID, sim_function(studentID, sID, database)))

    matches.sort(key=sort_by_sID, reverse=True)

    for i in range(len(matches) - n):
        if i >= 0:
            matches.pop(-i - 1)

    return matches

# I'm student 1890
results_euclidean = top_matches('student1890', test_db)
results_pearson = top_matches('student1890', test_db, 5, sim_pearson)

print(results_pearson)
print(results_euclidean)

print("EUCLIDEAN (HIGHEST):")
for i in range(2):
    print(f"{i + 1}. {results_euclidean[i][0]}")

print("PEARSON (HIGHEST):")
for i in range(2):
    print(f"{i + 1}. {results_pearson[i][0]}")

print("PEARSON (LOWEST):")
for i in range(2):
    print(f"{i + 1}. {results_pearson[-i][0]}")
