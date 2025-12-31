# Q:- Student Exam Scores Analysis
# Description:
# Simulate a class of 30 students and 5 subjects. Generate random scores, clean the data, analyze it, and extract insights.
# What it will teach / use:
# Array creation
# Random numbers
# Boolean masking / conditional operations
# Row/column operations
# Broadcasting
# Sorting and indexing
import numpy as np

# Step 1: Generate random scores for 30 students in 5 subjects (0-100)
scores = np.random.randint(0, 101, size=(30,5))
print("Original Scores:\n", scores)

# Step 2: If any student has a score < 35 in a subject, set it as 0 (fail)
scores[scores < 35] = 0
print("\nScores after setting failing marks to 0:\n", scores)

# Step 3: Calculate total and average scores for each student
total_scores = scores.sum(axis=1)
avg_scores = scores.mean(axis=1)
print("\nTotal Scores:", total_scores)
print("Average Scores:", avg_scores)

# Step 4: Identify top 3 students by total score
top_indices = np.argsort(total_scores)[-3:][::-1]
print("\nTop 3 students (by index):", top_indices)
print("Their total scores:", total_scores[top_indices])

# Step 5: Calculate average score for each subject
subject_avg = scores.mean(axis=0)
print("\nAverage score per subject:", subject_avg)

# Step 6: Bonus - Normalize the score matrix (0 to 1 scale)
normalized_scores = (scores - scores.min()) / (scores.max() - scores.min())
print("\nNormalized Scores:\n", normalized_scores)
