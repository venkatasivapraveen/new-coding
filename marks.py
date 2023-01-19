Python 3.3.0 (v3.3.0:bd8afb90ebf2, Sep 29 2012, 10:57:17) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> students = [['vam', 85, 90, 75],
            ['siv', 82, 98, 80],
            ['kick', 83, 86, 91],
            ['eswar', 89, 90, 76]
            ]
each_test_total = []
num_tests = len(students[0]) - 1
num_students = len(students)
for test_index in range(num_tests):
    each_test_total.append(0)
for student_index in range(num_students):
    for test_index in range(num_tests):
        each_test_total[test_index] += students[student_index][test_index + 1]
each_test_average = []
for test_index in range(num_tests):
    each_test_average.append(each_test_total[test_index]/len(students))
for test_index in range (num_tests):
    print('The average for test ' + str(test_index + 1)+ ' is ' +  str(each_test_average[test_index]))
