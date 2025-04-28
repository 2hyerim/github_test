import matplotlib.pyplot as plt
import numpy as np

def trap(height):
    if not height:
        return 0, []
    n = len(height)
    left, right = 0, n - 1
    left_max, right_max = height[left], height[right]
    water = 0
    water_trapped = [0] * n  # 각 위치에 저장된 물의 양

    while left < right:
        if height[left] < height[right]:
            left += 1
            left_max = max(left_max, height[left])
            trapped = left_max - height[left]
            water += trapped
            water_trapped[left] = trapped
        else:
            right -= 1
            right_max = max(right_max, height[right])
            trapped = right_max - height[right]
            water += trapped
            water_trapped[right] = trapped
    return water, water_trapped

def plot_trap(height):
    total_water, water_trapped = trap(height)
    x = np.arange(len(height))
    plt.figure(figsize=(8, 4))
    plt.bar(x, height, color='black', label='Ground')
    plt.bar(x, water_trapped, bottom=height, color='blue', label='Water')
    plt.title(f'Trapping Rain Water\nHeight = {height}\nTrapped Water = {total_water}')
    plt.xlabel('Index')
    plt.ylabel('Height')
    plt.legend()
    plt.show()

# 예시 1
example1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
plot_trap(example1)

# 예시 2
example2 = [4, 2, 0, 3, 2, 5]
plot_trap(example2)

# 예시 3
example3 = [2, 0, 2]
plot_trap(example3)
