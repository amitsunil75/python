# Given the names and grades for each student in a class of  students, store them in a nested
#  list and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the second lowest grade, order their names
#  alphabetically and print each name on a new line.

# Example

# The ordered list of scores is , so the second lowest score is . There are two students with that score: .
#  Ordered alphabetically, the names are printed as:

# alpha
# beta
# Input Format

# The first line contains an integer, , the number of students.
# The  subsequent lines describe each student over  lines.
# - The first line contains a student's name.
# - The second line contains their grade.

# Constraints

# There will always be one or more students having the second lowest grade.
# Output Format

# Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order their names alphabetically and print each one on a new line.

# Sample Input 0

# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39
# Sample Output 0

# Berry
# Harry
# Explanation 0

# There are  students in this class whose names and grades are assembled to build the following list:

# python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

# The lowest grade of  belongs to Tina. The second lowest grade of  belongs to both Harry and Berry, so we order their names alphabetically and print each name on a new line.




# matrix = [['rahul',20.1],['rahl',20.1],['raul',90],['ra',50],['rul',20.2]]
# # for _ in range(int(input())):
# #         name = input()
# #         score = float(input())
# #         matrix.append([name, score])
        
# matrix.sort(key=lambda x: x[1])
# print(matrix)
# print(matrix[1][0])
# print(matrix[0][0])


if __name__ == '__main__':
    students = [['rahul',20.1],['rahl',20.1],['raul',90],['ra',50],['rul',20.2]]
    
    # Read input for each student and store in the list
    # for _ in range(int(input())):
    #     name = input()
    #     score = float(input())
    #     students.append([name, score])
    
    # Sort the list of students by their scores
    students.sort(key=lambda x: x[1])
    print(students)
    
    # Find the second lowest grade
    second_lowest_grade = None
    lowest_grade = students[0][1]
    for _, score in students:
        if score != lowest_grade:
            second_lowest_grade = score
            break
    print( second_lowest_grade)
    # Collect names of students with the second lowest grade
    second_lowest_students = []
    for name, score in students:
        if score == second_lowest_grade:
            second_lowest_students.append(name)
    
    # Sort the names alphabetically
    second_lowest_students.sort()
    print(second_lowest_students)
    
    # Print the names of students with the second lowest grade
    for name in second_lowest_students:
        print(name)
