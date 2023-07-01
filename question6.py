from collections import defaultdict

def findOriginalArray(changed):
    count_dict = defaultdict(int)
    
    for num in changed:
        count_dict[num] += 1
    
    original = []
    
    for num in changed:
        if count_dict[num] == 0:
            continue
        
        if count_dict[2 * num] == 0:
            return []
        
        count_dict[2 * num] -= 1
        original.append(num)
    
    return original
changed = [1, 3, 4, 2, 6, 8]
print(findOriginalArray(changed))
