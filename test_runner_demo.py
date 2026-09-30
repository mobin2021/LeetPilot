"""
LeetPilot // Standalone CLI Test Runner & Benchmark Demo
Executes algorithm solutions against test cases with microsecond benchmarks.
Author: MD. Raisul Islam Mobin | mobin.tech
"""
import time

def two_sum_optimal(nums: list[int], target: int) -> list[int]:
    """Single-pass Hash Map: O(N) Time, O(N) Space"""
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

def run_test_suite():
    print("=" * 65)
    print("[*] LeetPilot // Algorithmic Benchmark & Assertion Runner")
    print("    Problem: Two Sum (Optimal Single-Pass Hash Map)")
    print("=" * 65)

    test_cases = [
        {"nums": [2, 7, 11, 15], "target": 9, "expected": [0, 1]},
        {"nums": [3, 2, 4], "target": 6, "expected": [1, 2]},
        {"nums": [3, 3], "target": 6, "expected": [0, 1]},
        {"nums": [1, 5, 8, 12, 19, 25, 30], "target": 44, "expected": [4, 5]},
    ]

    all_passed = True
    start_all = time.perf_counter()

    for idx, tc in enumerate(test_cases, 1):
        t0 = time.perf_counter()
        result = two_sum_optimal(tc["nums"], tc["target"])
        latency_us = (time.perf_counter() - t0) * 1_000_000

        passed = result == tc["expected"]
        if not passed:
            all_passed = False

        status_tag = "[PASS]" if passed else "[FAIL]"
        print(f"  Test Case #{idx}: {status_tag}")
        print(f"    Input:    nums={tc['nums']}, target={tc['target']}")
        print(f"    Output:   {result}")
        print(f"    Expected: {tc['expected']}")
        print(f"    Latency:  {latency_us:.2f} microseconds\n")

    total_time_ms = (time.perf_counter() - start_all) * 1000
    print("-" * 65)
    if all_passed:
        print(f"[ALL PASSED] 4/4 test cases passed in {total_time_ms:.3f} ms total.")
    else:
        print(f"[FAIL] Some test cases failed.")
    print("=" * 65)

if __name__ == "__main__":
    run_test_suite()
