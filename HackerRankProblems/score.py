# Given the participants' score sheet for your University Sports Day, 
# you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

# Input Format

# The first line contains . The second line contains an array   of  integers each separated by a space.

# Constraints

# Output Format

# Print the runner-up score.

# Sample Input 0

# 5
# 2 3 6 6 5
# Sample Output 0

# 5
# Explanation 0

# Given list is . The maximum score is , second maximum is . Hence, we print  as the runner-up score.

n = int(input())
    
    # Check if the number of scores is within the range [2, 10]
if 2 <= n <= 10:
        scores = list(map(int, input().split()))
        
        # Check if all scores are within the range [-100, 100]
        if all(-100 <= score <= 100 for score in scores):
            # Convert scores to a set to remove duplicates
            scores = set(scores)
            
            # Find the maximum score
            max_score = max(scores)
            
            # Remove the maximum score from the set
            scores.remove(max_score)
            
            # Find the runner-up score
            runner_up_score = max(scores)
            
            # Print the runner-up score
            print(runner_up_score)
        else:
            print("Error: Scores should be within the range [-100, 100].")
else:
        print("Error: Number of scores should be within the range [2, 10].")

