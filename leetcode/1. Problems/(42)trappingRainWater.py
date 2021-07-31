
height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6


def trap(height):
    if len(height) < 3:
        return 0
    mx = height[0]
    left = [0]
    for i in range(1, len(height)):
        if height[i] > mx:
            left.append(height[i])
            mx = height[i]
        else:
            left.append(mx)

    right = [0]    
    mx = height[-1]
    for i in range(len(height)-1, -1, -1):
        if height[i] > mx:
            right.append(height[i])
            mx = height[i]
        else:
            right.append(mx)
    right.reverse()

    output = 0
    for i in range(len(height)):
        if height[i] < left[i] and height[i] < right[i]:
            output += min(left[i], right[i]) - height[i]
    return output






print(trap(height))