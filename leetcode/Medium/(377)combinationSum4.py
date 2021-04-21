

nums = [1, 2, 3]
target = 4

def combinationSum4(nums, target):
    dp = [0]*(target+1)
    dp[0] = 1
    # print(f"Current DP={dp}, our target is {target}")
    for t in range(1, target+1):
        # print(f"Checking t={t} for t in range 1-{target+1}")
        for n in nums:
            # print(f"Checking n={n} for n in nums ({nums})")
            # print(f"Is {n} <= {t}")
            if n <= t:
                # print(f"Yes, {n} <= {t}")
                # print(f"Adding dp[{t}-{n}] to dp[{t}] i.e. adding {dp[t-n]} to {dp[t]}")
                dp[t]+=dp[t-n]
    #             print(f"New dp = {dp}")
    #     print(f"finished going through nums for t={t}")
    #     print(f"current dp={dp} meaning the whatever the biggest value in dp is how many sums are possible for the index of the dp")
    # print(f"finished everything")
    # print(f"final dp={dp}, and our answer is {dp[target]}")
    return dp[target]

print(combinationSum4(nums, target))



