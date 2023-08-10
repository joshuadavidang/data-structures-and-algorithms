from count_nice_subarray import numberOfSubarrays

tests = [
    {"query": [[1, 1, 2, 1, 1], 3], "output": 2},
    {"query": [[2, 4, 6], 1], "output": 0},
    {"query": [[2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2], "output": 16},
]

passed_cases = 0
failed_cases = 0
total_cases = len(tests)

for i, test in enumerate(tests):
    print(f"Test Case {i + 1}")
    print(f"Expected Output:", test["output"])
    result = numberOfSubarrays(test["query"][0], test["query"][1])
    print(f"Actual Output:", result)

    if result == test["output"]:
        print("------ PASSED ------ \n")
        passed_cases += 1
    else:
        print("------ FAILED ------ \n")
        failed_cases += 1

print("*" * 100, "\n")
print(f"Result: {passed_cases}/{total_cases} \n")
