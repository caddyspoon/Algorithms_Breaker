import heapq

def solution(operations):
    max_heap = []
    min_heap = []
    
    for operation in operations:
        comm, elm = operation.split()
        elm = int(elm)
        
        if comm == "I":
            heapq.heappush(max_heap, -elm)
            heapq.heappush(min_heap, elm)

        elif comm == "D" and elm == 1:
            if max_heap:
                max_elm = -heapq.heappop(max_heap)
                min_heap.remove(max_elm)

        elif comm == "D" and elm == -1:
            if min_heap:
                min_elm = heapq.heappop(min_heap)
                max_heap.remove(-min_elm)
    
    if len(max_heap) == 0:
        return [0, 0]
    else:
        return [-heapq.heappop(max_heap), heapq.heappop(min_heap)]
    
# # case 1.
operations = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
result = [0,0]

# # case 2.
# operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
# result = [333, -45] 

print(solution(operations), solution(operations) == result)