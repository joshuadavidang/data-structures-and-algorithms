from decode_message import decodeMessage

tests = [
    {
        "query": ["the quick brown fox jumps over the lazy dog", "vkbs bs t suepuv"],
        "output": "this is a secret",
    },
    {
        "query": ["eljuxhpwnyrdgtqkviszcfmabo", "zwx hnfx lqantp mnoeius ycgk vcnjrdb"],
        "output": "the five boxing wizards jump quickly",
    },
]

passed_cases = 0
failed_cases = 0
total_cases = len(tests)

for i, test in enumerate(tests):
    print(f"Test Case {i + 1}")
    print(f"Expected Output:", test["output"])
    result = decodeMessage(test["query"][0], test["query"][1])
    print(f"Actual Output:", result)

    if result == test["output"]:
        print("------ PASSED ------ \n")
        passed_cases += 1
    else:
        print("------ FAILED ------ \n")
        failed_cases += 1

print("*" * 100, "\n")
print(f"Result: {passed_cases}/{total_cases} \n")
