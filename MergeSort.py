def mergesort(sequence):
   if len(sequence) <= 1:
       return sequence[:]
   else:
       mid = len(sequence) // 2

       left = mergesort(sequence[:mid])
       right = mergesort(sequence[mid:])

       return merge(left, right)

def merge(list1, list2):
    merged=[]
    l=0
    r=0
    while l<len(list1) and r<len(list2):
        if list1[l]<list2[r]:
            merged.append(list1[l])
            l+=1
        else:
            merged.append(list2[r])
            r+=1
    while r<len(list2) or l<len(list1):
        if r<len(list2):
            merged.append(list2[r])
            r+=1
        else:
            merged.append(list1[l])
            l+=1
    return merged
print(merge([1,5,5,11],[0,10,10,13]))

