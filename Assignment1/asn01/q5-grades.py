# Read from a file with student grades.
# Each line has:
# Student ID, Course number, Score (score is an int, 0 through 100).

# Your goal: Compute each student's GPA.
# Print, one per line:
# Student ID, average score, GPA.
#
# Use this grading scale:
# Score:       ≥94 ≥90 ≥87 ≥84 ≥80 ≥77 ≥74 ≥70 ≥67 ≥64 ≥60 <60
# Grade points: 4  3.7 3.3 3.0 2.7 2.3 2.0 1.7 1.3 1.0 0.7 0.0
#
# Assumption: All courses have the same # of credits (say they're all 3 credits)

import sys

def main():
    if len(sys.argv) != 2:
        print("Usage:")
        print("  python q5-grades.py <grade-file.csv>")
        sys.exit(1)
    file_name = sys.argv[1]

    # 1. Read the file.
    # 2. Gather each student's scores
    # 3. Compute each student's average score
    # 4. Convert the score to a GPA, and print results

if __name__ == '__main__':
    main()
