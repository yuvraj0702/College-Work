def find_runner_up_score(scores):
    # Sort the list of scores in descending order
    sorted_scores = sorted(scores, reverse=True)
    
    # Find the second highest score
    runner_up_score = sorted(set(sorted_scores), reverse=True)[1]
    
    return runner_up_score

# Example usage:
if __name__ == "__main__":
    N = int(input("Enter the number of students: "))
    scores = list(map(int, input("Enter the scores separated by space: ").split()))
    
    runner_up_score = find_runner_up_score(scores)
    print("Runner-up score:", runner_up_score)
