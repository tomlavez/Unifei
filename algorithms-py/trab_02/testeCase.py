import subprocess, time

test_cases = ["580000 3", "560000 3", "550000 5", "550000 6", "540000 7", "545000 4"]
media = 0

for test in test_cases:
    start = time.time()
    result = subprocess.run(
        ["python3", "dicts.py"], input=test, text=True, capture_output=True
    )
    print(f"Test case ({test}): {result.stdout}")
    end = time.time()
    print(f"Execution time: {end - start}")
    media += end - start
    print()

print(f"Average execution time: {media / len(test_cases)}")
