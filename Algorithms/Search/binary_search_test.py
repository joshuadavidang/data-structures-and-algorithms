from binary_search import DSA

tests = [
    {
        "name": "Query found in list book",
        "input": {"book_no": [1, 3, 5, 7, 11, 23, 35, 55, 56, 61], "query": 5},
        "output": 2,
    },
    {
        "name": "Query found in the first element",
        "input": {"book_no": [1, 3, 5, 7, 11, 23, 35, 55, 56, 61], "query": 1},
        "output": 0,
    },
    {
        "name": "Query found in the last element",
        "input": {"book_no": [1, 3, 5, 7, 11, 23, 35, 55, 56, 61], "query": 61},
        "output": 9,
    },
    {
        "name": "Query is the only element",
        "input": {"book_no": [5], "query": 5},
        "output": 0,
    },
    {
        "name": "Query not found in list book",
        "input": {"book_no": [1, 3, 5, 7, 11, 23, 35, 55, 56, 61], "query": 50},
        "output": -1,
    },
]

passed_cases = 0
failed_cases = 0
total_tests = len(tests)
dsa_instance = DSA("algorithm", "binary_search")

for index, test in enumerate(tests):
    result = dsa_instance.binary_search(
        tests[index]["input"]["book_no"], tests[index]["input"]["query"]
    )
    print(f"Test Case {index + 1}:", tests[index]["name"])
    print()

    print("Input:")
    print(tests[index]["input"])
    print()

    print("Expected Output:")
    print(tests[index]["output"])
    print()

    print("Actual Output:")
    print(result)
    print()

    print("Test Result:")
    if tests[index]["output"] == result:
        print("PASSED")
        passed_cases += 1
    else:
        print("FAILED")
        failed_cases += 1

    print()
    print("*" * 100)
    print()

print(f"Result: {passed_cases}/{total_tests}")
