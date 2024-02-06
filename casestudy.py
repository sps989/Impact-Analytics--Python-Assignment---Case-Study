# In a university, your attendance determines whether you will be allowed to attend
# your graduation ceremony. You are not allowed to miss classes for four or more consecutive days.
# Your graduation ceremony is on the last day of the academic year, which is the Nth day. Your task is
# to determine the following:
#
# 1. The number of ways to attend classes over N days.
# 2. The probability that you will miss your graduation ceremony.
#
# Represent the solution in the string format as "Answer of (2) / Answer
# of (1)", don't actually divide or reduce the fraction to decimal Test cases:
#
# for 5 days: 14/29
# for 10 days: 372/773

def graduation_ceremony_probability(N):
    ways_to_attend = [0] * (N + 1)

    ways_to_attend[1] = 1

    for i in range(2, N + 1):
        ways_to_attend[i] = ways_to_attend[i - 1] + ways_to_attend[i - 2]

    total_ways_to_attend = sum(ways_to_attend)

    probability_missing = total_ways_to_attend - ways_to_attend[N]

    result_string = f"{probability_missing}/{total_ways_to_attend}"

    return result_string

# Test cases
print(graduation_ceremony_probability(5))
print(graduation_ceremony_probability(10))
"Time complexity for above solution is O(N) and space complexity also O(N)"


def graduation_ceremony_probability(N):
    if N == 1:
        return "0/1"

    ways_to_attend_prev = 1
    ways_to_attend_current = 1

    for i in range(2, N + 1):
        ways_to_attend_next = ways_to_attend_current + ways_to_attend_prev

        ways_to_attend_prev = ways_to_attend_current
        ways_to_attend_current = ways_to_attend_next

    total_ways_to_attend = ways_to_attend_current + ways_to_attend_prev

    probability_missing = total_ways_to_attend - ways_to_attend_current

    result_string = f"{probability_missing}/{total_ways_to_attend}"

    return result_string

# Test cases
print(graduation_ceremony_probability(5))
print(graduation_ceremony_probability(10))
"Time complexity for above is is O(N) and space complexity also O(1) "
