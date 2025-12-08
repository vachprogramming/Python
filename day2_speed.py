from __future__ import annotations
from typing import List, Dict
import random
import time


# -------------------------------------------------------
# 1. DATA GENERATION
# -------------------------------------------------------
def generate_data(size: int) -> List[int]:
    """Generate a list of random integers between 1 and 100,000."""
    return [random.randint(1, 100_000) for _ in range(size)]


# -------------------------------------------------------
# 2. SLOW VERSION — USING ONLY A LIST (O(n²))
# -------------------------------------------------------
def count_duplicates_list(data: List[int]) -> int:
    """
    Count how many distinct numbers appear more than once.
    This version uses ONLY lists — intentionally slow.

    Logic:
      - seen: stores numbers we've encountered
      - duplicates: stores numbers we counted as duplicates
    """
    seen: List[int] = []
    duplicates: List[int] = []
    count: int = 0

    for num in data:

        # O(n) membership test → extremely slow for large lists
        if num in seen:

            # Ensure we only count a duplicate *once*
            if num not in duplicates:
                duplicates.append(num)
                count += 1

        else:
            seen.append(num)

    return count


# -------------------------------------------------------
# 3. FAST VERSION — USING A DICTIONARY (O(n))
# -------------------------------------------------------
def count_duplicates_dict(data: List[int]) -> int:
    """
    Count how many distinct numbers appear more than once.
    Uses a dictionary for O(1) access.
    """
    counts: Dict[int, int] = {}

    for num in data:
        # Dict access is O(1)
        counts[num] = counts.get(num, 0) + 1

    # Count how many items appear more than once
    return sum(1 for c in counts.values() if c > 1)


# -------------------------------------------------------
# 4. BENCHMARK
# -------------------------------------------------------
if __name__ == "__main__":
    SIZE = 20_000
    data = generate_data(SIZE)

    print(f"\nBenchmarking duplicate counters with dataset of {SIZE:,} integers...\n")

    # ---- Slow list version ----
    start = time.time()
    dup_list = count_duplicates_list(data)
    list_time = time.time() - start

    # ---- Fast dict version ----
    start = time.time()
    dup_dict = count_duplicates_dict(data)
    dict_time = time.time() - start

    # ---- Output ----
    print(f"List Version (O(n²))  : {list_time:.4f} sec — Duplicates: {dup_list}")
    print(f"Dict Version (O(n))   : {dict_time:.4f} sec — Duplicates: {dup_dict}")

    if dict_time > 0:
        speedup = list_time / dict_time
        print(f"\n➡ Dictionary was approximately {speedup:.1f}x faster.\n")
    else:
        print("\nDict version was too fast to measure!\n")
