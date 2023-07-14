from search_2d import searchMatrix

tests = [
    {"query": [[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3], "output": True},
    {
        "query": [[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13],
        "output": False,
    },
]

passed_cases = 0
failed_cases = 0
total_cases = len(tests)

for i, test in enumerate(tests):
    print(f"Test Case {i + 1}")
    print(f"Expected Output:", test["output"])
    result = searchMatrix(test["query"][0], test["query"][1])
    print(f"Actual Output:", result)

    if result == test["output"]:
        print("------ PASSED ------ \n")
        passed_cases += 1
    else:
        print("------ FAILED ------ \n")
        failed_cases += 1

print("*" * 100, "\n")
print(f"Result: {passed_cases}/{total_cases} \n")
