from max_sum import max_sum

tests = [
    {"query": [[100, 200, 300, 400], 2], "output": 700},
    {"query": [[1, 4, 2, 10, 23, 3, 1, 0, 20], 4], "output": 39},
    {"query": [[2, 3], 3], "output": -1},
]

passed_cases = 0
failed_cases = 0
total_cases = len(tests)

for i, test in enumerate(tests):
    print(f"Test Case {i + 1}")
    print(f"Expected Output:", test["output"])
    result = max_sum(test["query"][0], test["query"][1])
    print(f"Actual Output:", result)

    if result == test["output"]:
        print("------ PASSED ------ \n")
        passed_cases += 1
    else:
        print("------ FAILED ------ \n")
        failed_cases += 1

print("*" * 100, "\n")
print(f"Result: {passed_cases}/{total_cases} \n")
