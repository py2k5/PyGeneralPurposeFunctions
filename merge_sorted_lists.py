
##merge two sorted lists and return
##input [1,2,5,20], [4,6,7,8]
##output: [1,2,4,5,6,7,8,20]
## 

def merge_lists(l1,l2):
  
  ## take indexes to both arrays
  ## compare them ....
  ### if equal just copy
  ## if list1 is greater increment index of list 2
  ## and vice versa
  
  sorted_list = []
  while (l1 and l2):
        if (l1[0] <= l2[0]): # Compare both heads
            item = l1.pop(0) # Pop from the head
            sorted_list.append(item)
        else:
            item = l2.pop(0)
            sorted_list.append(item)
            
  sorted_list.extend(l1 if l1 else l2)
  return sorted_list    
      
print(merge_lists([1,2,20], [4,6,7,8]))
