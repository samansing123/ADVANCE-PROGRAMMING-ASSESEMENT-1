import random

# Ask the user to pick a difficulty level
def selectDifficulty():
    print("DIFFICULTY LEVEL")
    print("1. Easy")
    print("2. Moderate")
    print("3. Advanced")
    
    while True:
        try:
            choice = int(input("Choose difficulty (1–3): "))
            if choice in [1, 2, 3]:
                return choice
            else:
                print("Please enter 1, 2, or 3.")
        except:
            print("Invalid input. Please enter a number.")

# Generate numbers based on the selected difficulty
def generateRandomNumber(level):
    if level == 1:
        return random.randint(1, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(1000, 9999)

# Randomly choose addition or subtraction
def chooseOperation():
    return random.choice(['+', '-'])

# Display a problem and get the user’s answer
def presentProblem(num1, num2, op):
    print()
    print(f"{num1} {op} {num2} = ", end="")
    
    while True:
        try:
            answer = int(input())
            return answer
        except:
            print("Please enter a valid number.")
            print(f"{num1} {op} {num2} = ", end="")

# Check the user's answer and award points
def checkAnswer(userAns, correctAns, attempt):
    if userAns == correctAns:
        if attempt == 1:
            print("Correct! +10 points")
            return 10
        else:
            print("Correct on second try! +5 points")
            return 5
    else:
        if attempt == 1:
            print("Incorrect. Try again.")
        else:
            print(f"Wrong again! The correct answer was {correctAns}.")
        return 0

# Show the final score and grade
def showResults(score):
    print("\nQUIZ COMPLETE!")
    print(f"Your final score is {score}/100")
    
    if score >= 90:
        grade = "A+"
    elif score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    elif score >= 50:
        grade = "D"
    else:
        grade = "F"
    
    print("Your grade:", grade)
    print()

# Run the full quiz
def startQuiz():
    level = selectDifficulty()
    totalScore = 0

    for i in range(1, 11):
        num1 = generateRandomNumber(level)
        num2 = generateRandomNumber(level)
        op = chooseOperation()

        # Avoid negative answers for subtraction
        if op == '-' and num1 < num2:
            num1, num2 = num2, num1

        # Calculate correct answer
        correctAns = num1 + num2 if op == '+' else num1 - num2

        print(f"\nQuestion {i}:")
        attempt = 1

        # First attempt
        userAns = presentProblem(num1, num2, op)
        score = checkAnswer(userAns, correctAns, attempt)

        # Second attempt if needed
        if score == 0 and userAns != correctAns:
            attempt = 2
            userAns = presentProblem(num1, num2, op)
            score = checkAnswer(userAns, correctAns, attempt)

        totalScore += score

    showResults(totalScore)

# Main program loop
def main():
    print("Welcome to the Math Quiz Generator!")
    
    while True:
        startQuiz()
        again = input("Do you want to play again? (y/n): ").lower()
        if again != 'y':
            print("Thanks for playing!")
            break

main()
