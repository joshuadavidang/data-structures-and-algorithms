from cells_in_range import cellsInRange

tests = [
    {"query": "K1:L2", "output": ["K1", "K2", "L1", "L2"]},
    {"query": "A1:F1", "output": ["A1", "B1", "C1", "D1", "E1", "F1"]},
]

passed_cases = 0
failed_cases = 0
total_cases = len(tests)

for i, test in enumerate(tests):
    print(f"Test Case {i + 1}")
    print(f"Expected Output:", test["output"])
    result = cellsInRange(test["query"])
    print(f"Actual Output:", result)

    if result == test["output"]:
        print("------ PASSED ------ \n")
        passed_cases += 1
    else:
        print("------ FAILED ------ \n")
        failed_cases += 1

print("*" * 100, "\n")
print(f"Result: {passed_cases}/{total_cases} \n")
