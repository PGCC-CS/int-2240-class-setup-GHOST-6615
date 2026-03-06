# Function to calculate average
def calculateAverage(score1, score2, score3):
    average = (score1 + score2 + score3) / 3
    return round(average, 2)


# Function to determine letter grade
def getLetterGrade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


# Function to determine academic standing
def getAcademicStanding(letter):
    if letter == "A":
        return "Excellent"
    elif letter == "B":
        return "Good"
    elif letter == "C":
        return "Satisfactory"
    elif letter == "D":
        return "Needs Improvement"
    else:
        return "Failing"


# Main function
def main():

    # Ask user for scores
    score1 = float(input("Enter first test score: "))
    score2 = float(input("Enter second test score: "))
    score3 = float(input("Enter third test score: "))

    # Validate scores
    if score1 < 0 or score1 > 100 or score2 < 0 or score2 > 100 or score3 < 0 or score3 > 100:
        print("Invalid scores. Scores must be between 0 and 100.")
        return

    # Calculate results
    average = calculateAverage(score1, score2, score3)
    letter = getLetterGrade(average)
    standing = getAcademicStanding(letter)

    # Display results
    print("Average score:", average)
    print("Letter grade:", letter)
    print("Academic Standing:", standing)


# Run the program
main()