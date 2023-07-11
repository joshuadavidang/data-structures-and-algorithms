from is_anagram import is_anagram

tests = [
    {
        "test_case": "Both lengths are equal",
        "query_one": "anagram",
        "query_two": "nagaram",
        "output": True,
    },
    {
        "test_case": "Both lengths are not equal",
        "query_one": "rat",
        "query_two": "car",
        "output": False,
    },
]

passed_cases = 0
failed_cases = 0
total_cases = len(tests)

for i, test in enumerate(tests):
    print(f"Test Case {i + 1}:", test["test_case"])
    print(f"Expected Output:", test["output"])
    result = is_anagram(test["query_one"], test["query_two"])
    print(f"Actual Output:", result)

    if result == test["output"]:
        print("------ PASSED ------ \n")
        passed_cases += 1
    else:
        print("------ FAILED ------ \n")
        failed_cases += 1

print("*" * 100, "\n")
print(f"Result: {passed_cases}/{total_cases} \n")
