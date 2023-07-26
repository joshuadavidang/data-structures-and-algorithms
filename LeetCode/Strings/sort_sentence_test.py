from sort_sentence import sortSentence

tests = [
    {"query": "is2 sentence4 This1 a3", "output": "This is a sentence"},
    {"query": "Myself2 Me1 I4 and3", "output": "Me Myself and I"},
]

passed_cases = 0
failed_cases = 0
total_cases = len(tests)

for i, test in enumerate(tests):
    print(f"Test Case {i + 1}")
    print(f"Expected Output:", test["output"])
    result = sortSentence(test["query"])
    print(f"Actual Output:", result)

    if result == test["output"]:
        print("------ PASSED ------ \n")
        passed_cases += 1
    else:
        print("------ FAILED ------ \n")
        failed_cases += 1

print("*" * 100, "\n")
print(f"Result: {passed_cases}/{total_cases} \n")
