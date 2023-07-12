from group_anagram import group_anagram

tests = [
    {
        "query": ["eat", "tea", "tan", "ate", "nat", "bat"],
        "output": [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]],
    },
    {"query": [""], "output": [[""]]},
    {"query": ["a"], "output": [["a"]]},
]

passed_cases = 0
failed_cases = 0
total_cases = len(tests)

for i, test in enumerate(tests):
    print(f"Test Case {i + 1}")
    print(f"Expected Output:", test["output"])
    result = group_anagram(test["query"])
    print(f"Actual Output:", result)

    if result == test["output"]:
        print("------ PASSED ------ \n")
        passed_cases += 1
    else:
        print("------ FAILED ------ \n")
        failed_cases += 1

print("*" * 100, "\n")
print(f"Result: {passed_cases}/{total_cases} \n")
