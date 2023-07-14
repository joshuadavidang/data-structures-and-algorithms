from two_sum_II import two_sum

tests = [
    {
        "query": [[2, 7, 11, 15], 9],
        "output": [1, 2],
    },
    {
        "query": [[2, 3, 4], 6],
        "output": [1, 3],
    },
    {
        "query": [[3, 3], 6],
        "output": [1, 2],
    },
]

passed_cases = 0
failed_cases = 0
total_cases = len(tests)

for i, test in enumerate(tests):
    print(f"Test Case {i + 1}")
    print(f"Expected Output:", test["output"])
    result = two_sum(test["query"][0], test["query"][1])
    print(f"Actual Output:", result)

    if result == test["output"]:
        print("------ PASSED ------ \n")
        passed_cases += 1
    else:
        print("------ FAILED ------ \n")
        failed_cases += 1

print("*" * 100, "\n")
print(f"Result: {passed_cases}/{total_cases} \n")
