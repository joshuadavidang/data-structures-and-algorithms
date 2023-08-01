from find_anagrams import findAnagrams

tests = [
    {"query": ["cbaebabacd", "abc"], "output": [0, 6]},
    {"query": ["abab", "ab"], "output": [0, 1, 2]},
]

passed_cases = 0
failed_cases = 0
total_cases = len(tests)

for i, test in enumerate(tests):
    print(f"Test Case {i + 1}")
    print(f"Expected Output:", test["output"])
    result = findAnagrams(test["query"][0], test["query"][1])
    print(f"Actual Output:", result)

    if result == test["output"]:
        print("------ PASSED ------ \n")
        passed_cases += 1
    else:
        print("------ FAILED ------ \n")
        failed_cases += 1

print("*" * 100, "\n")
print(f"Result: {passed_cases}/{total_cases} \n")
