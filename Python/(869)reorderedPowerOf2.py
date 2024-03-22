




def reorderedPowerOf2(n: int) -> bool:
    power = 1
    while power <= 10**9:
        if sorted(str(power)) == sorted(str(n)):
            return True
        power *= 2
    return False



print(f"Answer: {reorderedPowerOf2(n=2)}. Should be True")
print(f"Answer: {reorderedPowerOf2(n=10)}. Should be False")
print(f"Answer: {reorderedPowerOf2(n=124)}. Should be False")
print(f"Answer: {reorderedPowerOf2(n=2408)}. Should be True")

