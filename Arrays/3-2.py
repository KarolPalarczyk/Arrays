import random

arr1 = [3, 7, 1, 0, 4]
print(f"arr1: {arr1}")
arr2 = [[2, 3], [7, 1], [0, 4]]
print(f"arr2: {arr2}")
arr3 = [7 for i in range(5)]
print(f"arr3: {arr3}")
arr4 = [i for i in range(1, 10)]
print(f"arr4: {arr4}")
arr5 = [i * 2 for i in range(1, 10)]
print(f"arr5: {arr5}")
arr6 = [random.randint(1, 20) for i in range(10)]
print(f"arr6: {arr6}")
arr7 = [[i] for i in range(5)]
print(f"arr7: {arr7}")
arr8 = [[1 for i in range(2)] for j in range(4)]
print(f"arr8: {arr8}")
arr9 = [[random.randint(1, 20) for i in range(3)] for j in range(5)]
print(f"arr9: {arr9}")
arr10 = [4, 0, 3]
print(f"arr10: {arr10}")
arr11 = [0 for _ in range(15)]
print(f"arr11: {arr11}")
arr12 = [random.randint(1, 30) for _ in range(5)]
print(f"arr12: {arr12}")
arr13 = [random.randint(0, 1) for _ in range(20)]
print(f"arr13: {arr13}")
arr14 = [[False for _ in range(2)] for _ in range(5)]
print(f"arr14: {arr14}")