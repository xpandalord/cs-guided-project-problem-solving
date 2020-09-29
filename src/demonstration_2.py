"""
Given an integer value `n`, write a function that will return a list of the string representation of numbers from 1 to `n`.

However, there are a few additional rules to follow:

- For multiples of three, it should output "Lambda" instead of the number.
- For multiples of five, it should output "School" instead of the number.
- For numbers which are multiples of three and five, it should output "LambdaSchool" instead of the number.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Lambda",
    "4",
    "School",
    "Lambda",
    "7",
    "8",
    "Lambda",
    "School",
    "11",
    "Lambda",
    "13",
    "14",
    "LambdaSchool"
]
"""
def lambda_school(n):
    # Your code here
    answer = [] 

    # loop up to n, using `range` 
    # keep in mind we want 1-indexed numbers, instead of 0-indexing 
    for num in range(1, n+1):
        # we need to check if num is divisible by 3
        divisible_by_3 = (num % 3 == 0)
        # we need to check if num is divisible by 5
        divisible_by_5 = (num % 5 == 0)
        # we need to check if num is divisible by 3 and 5 

        # ordering of how we check divisibility of num is important 
        if divisible_by_3 and divisible_by_5:
            answer.append("LambdaSchool")
        elif divisible_by_3:
            answer.append("Lambda")
        elif divisible_by_5:
            answer.append("School")

        # for every other number, we need to push it to our answer
        # list, but as a string, instead of as a number 
        else:
            answer.append(str(num))

    return answer
    
print(lambda_school(30))