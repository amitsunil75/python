try:
    marks = int(input('Please enter your marks: '))
except ValueError:
    print("Invalid input! Please enter a valid integer for marks.")
else:
    # Your logic for processing the marks goes here
    if marks >100 or marks <0:
        print("invallid marks")
    elif marks >= 90 and marks<=100:
        print("Excellent! You scored an A.")
    elif marks >= 80 and marks<=90:
        print("Good! You scored a B.")
    elif marks >= 70 and marks<=80:
        print("Fair! You scored a C.")
    elif marks >= 60 and marks<=70:
        print("You scored a D.")
    else:
        print("You failed.")
        
