from gas_station import canCompleteCircuit

tests = [
    {"query": [[1, 2, 3, 4, 5], [3, 4, 5, 1, 2]], "output": 3},
    {"query": [[2, 3, 4], [3, 4, 3]], "output": -1},
]

passed_cases = 0
failed_cases = 0
total_cases = len(tests)

for i, test in enumerate(tests):
    print(f"Test Case {i + 1}")
    print(f"Expected Output:", test["output"])
    result = canCompleteCircuit(test["query"][0], test["query"][1])
    print(f"Actual Output:", result)

    if result == test["output"]:
        print("------ PASSED ------ \n")
        passed_cases += 1
    else:
        print("------ FAILED ------ \n")
        failed_cases += 1

print("*" * 100, "\n")
print(f"Result: {passed_cases}/{total_cases} \n")
