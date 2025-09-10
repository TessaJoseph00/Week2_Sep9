import numpy as np

#1
def ways(n):
    """
    Calculates the number of ways to make change for `n` cents using only pennies (1 cent) and nickels (5 cents).
    
    Parameters:
        n (int): The amount of cents to make change for.
    
    Returns:
        int: The number of unique combinations of pennies and nickels that sum to `n` cents.
    """
    
    # Initialize the counter for valid combinations
    count = 0

    # Iterate over all possible numbers of nickels (from 0 up to n // 5)
    for nickels in range(n // 5 + 1):
        
        # The rest of the amount is made up of pennies
        pennies = n - 5 * nickels

        # Count the valid combination
        count += 1

    return count
print("\n1. ")
print("n=12 ->",ways(12))                     
print("n=20 ->",ways(20))  
print("n=3  ->",ways(3))
print("n=0  ->",ways(0))

#2.a
def lowest_score(names, scores):
    """
    Finds the name of the student with the lowest test score.

    Parameters:
        names (numpy.ndarray): Array of student names.
        scores (numpy.ndarray): Array of test scores corresponding to each student.

    Returns:
        str: The name of the student with the lowest score.
    """
    # Find the index of the minimum score using np.argmin
    lowest_index = np.argmin(scores)
    
    # Return the name at the index of the minimum score
    return names[lowest_index]

names = np.array(['Hannah', 'Astrid', 'Abdul', 'Mauve', 'Jung'])
scores = np.array([99, 71, 85, 62, 91])
print("\n2.a  Student with lowest score:", lowest_score(names, scores))


#2.b

def sort_names(names, scores):
    """
    Sorts student names based on their test scores in descending order.

    Parameters:
        names (numpy.ndarray): Array of student names.
        scores (numpy.ndarray): Array of test scores corresponding to each student.

    Returns:
        numpy.ndarray: Array of names sorted by score from highest to lowest.
    """
    # Get the indices that would sort scores in descending order
    sorted_indices = np.argsort(scores)[::-1]

    # Return names arranged according to sorted score indices
    return names[sorted_indices]

print("\n2.b  Names sorted by descending scores:", sort_names(names, scores))
