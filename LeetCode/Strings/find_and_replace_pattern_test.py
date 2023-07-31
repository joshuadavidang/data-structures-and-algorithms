from find_and_replace_pattern import findAndReplacePattern

tests = [
    {
        "query": [["abc", "deq", "mee", "aqq", "dkd", "ccc"], "abb"],
        "output": ["mee", "aqq"],
    },
    {
        "query": [["a", "b", "c"], "a"],
        "output": ["a", "b", "c"],
    },
]

passed_cases = 0
failed_cases = 0
total_cases = len(tests)

for i, test in enumerate(tests):
    print(f"Test Case {i + 1}")
    print(f"Expected Output:", test["output"])
    result = findAndReplacePattern(test["query"][0], test["query"][1])
    print(f"Actual Output:", result)

    if result == test["output"]:
        print("------ PASSED ------ \n")
        passed_cases += 1
    else:
        print("------ FAILED ------ \n")
        failed_cases += 1

print("*" * 100, "\n")
print(f"Result: {passed_cases}/{total_cases} \n")
