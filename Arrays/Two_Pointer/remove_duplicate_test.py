from remove_duplicate import remove_duplicates

tests = [
    {"test_case": "Empty array []", "query": [], "output": 0},
    {"test_case": "One element in array [5]", "query": [5], "output": 1},
    {"test_case": "No duplicate element [1,2,3]", "query": [1, 2, 3], "output": 3},
    {"test_case": "Remove duplicate element [1,1,2]", "query": [1, 1, 2], "output": 2},
    {
        "test_case": "Remove duplicate element [0,0,1,1,1,2,2,3,3,4]",
        "query": [0, 0, 1, 1, 1, 2, 2, 3, 3, 4],
        "output": 5,
    },
]

passed_cases = 0
failed_cases = 0
total_cases = len(tests)

for i, test in enumerate(tests):
    print(f"Test Case {i + 1}:", test["test_case"])
    print(f"Expected Output:", test["output"])
    result = remove_duplicates(test["query"])
    print(f"Actual Output:", result)

    if result == test["output"]:
        print("------ PASSED ------ \n")
        passed_cases += 1
    else:
        print("------ FAILED ------ \n")
        failed_cases += 1

print("*" * 100, "\n")
print(f"Result: {passed_cases}/{total_cases} \n")
