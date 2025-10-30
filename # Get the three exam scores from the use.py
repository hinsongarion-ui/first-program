# Get the three exam scores from the user
score_A = float(input("Enter the score for Exam A: "))
score_B = float(input("Enter the score for Exam B: "))
score_C = float(input("Enter the score for Exam C: "))

# Calculate the average score
average = (score_A + score_B + score_C) / 3

# Print the average
print(f"\nAverage score: {average:.2f}")

# Determine if the student is approved
if average >= 7:
    print("Status: Approved ✅")
else:
    print("Status: Not Approved ❌")
