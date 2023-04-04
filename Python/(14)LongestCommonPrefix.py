""" 
Atanas Delevski
1/28/2023
LeetCode - Challange #14
"""
import time 

# Answer = "fl"
input1 = ["flower", "flow", "flight"]


def exec(input):
    ans = 0 
    for i in range(len(min(input))):
        our_set = set([f[i] for f in input])
        if len(list(our_set)) > 1:
            return input[0][:ans]
        else:
            ans += 1
    return input[0][:ans]


def main():
    # Init
    input = input1

    # Execution
    answer = exec(input)

    # Print
    print(f"Answer: {answer}")


if __name__ == "__main__":
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    print(f"Execution Time: {end-start} seconds.")

