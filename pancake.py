


def pancakeSort(nums, pre_swap, paths):
    
    global min_path
    
    cur_len = len(paths)
    
    if cur_len > min_path:
        return
    
    if cur_len > 10*len(nums):
        return
    
    if is_sorted(nums):
        res.append(paths.copy())
        if cur_len < min_path:
            min_path = cur_len
        return
    
    for i in range(1, len(nums)):
        if (i+1) == pre_swap:
            continue
            
        paths.append(i+1)
        tmp=swap(0, i+1, nums)
        
        pancakeSort(tmp, i+1, paths)
        
        paths.pop()


min_path=100000

nums=[3,2,4,1]
res = []
pancakeSort(nums, -1, [])
