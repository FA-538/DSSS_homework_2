import random


def function_random_value(min_val, max_val):
    """
    This function will generate a random value from the given minimum and maximum value.
    """
    return random.randint(min_val, max_val)


def function_operator():
    """
    This function generates a random operator from the given options.
    """
    return random.choice(['+', '-', '*', '/'])


def function_calculate(number1, number2, operator):
    problem = f"{number1} {operator} {number2}"
    if operator == '+':
        ans = number1 + number2
    elif operator == '-':
        ans = number1 - number2
    elif operator == '*':
        ans = number1 * number2
    else:
        if number2 == 0 and operator == '/':
            print("Error: Division By Zero is not allowed.")
            return None
        ans = number1 / number2
    return problem, ans


def math_quiz():
    score = 0
    total_question = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_question):
        n1 = function_random_value(1, 10)
        n2 = function_random_value(1, 5)  # changed the max value to an integer
        o = function_operator()

        problem, answer = function_calculate(n1, n2, o)
        if answer is None:
            continue  # Skip this question if there was a division by zero

        print(f"\nQuestion: {problem}")
        user_answer = input("Your answer: ")
        try:
            user_answer = float(user_answer)  # Allowing float input for division
        except ValueError:
            print("Please enter a valid number.")
            continue

        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    
    final_score =score/total_question 
    print(f"\nGame over! Your score is: {final_score}")


if __name__ == "__main__":
    math_quiz()
