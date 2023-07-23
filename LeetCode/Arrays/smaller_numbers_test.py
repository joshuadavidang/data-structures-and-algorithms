from smaller_numbers import smallerNumbersThanCurrent

tests = [
    {"query": [8, 1, 2, 2, 3], "output": [4, 0, 1, 1, 3]},
    {"query": [6, 5, 4, 8], "output": [2, 1, 0, 3]},
    {"query": [7, 7, 7, 7], "output": [0, 0, 0, 0]},
]

passed_cases = 0
failed_cases = 0
total_cases = len(tests)

for i, test in enumerate(tests):
    print(f"Test Case {i + 1}")
    print(f"Expected Output:", test["output"])
    result = smallerNumbersThanCurrent(test["query"])
    print(f"Actual Output:", result)

    if result == test["output"]:
        print("------ PASSED ------ \n")
        passed_cases += 1
    else:
        print("------ FAILED ------ \n")
        failed_cases += 1

print("*" * 100, "\n")
print(f"Result: {passed_cases}/{total_cases} \n")
