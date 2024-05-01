  """
2.1 Insertion Sort
array is input, True of Set represent the number of it increasing
"""
def insertionSort(Array:list,Set:bool) -> list:
    if Set == True:
        for i in range(1,len(Array)):
            key = Array[i]
            """Insert Array[i] into the sorted subarray Array[1:i-1]"""
            j = i-1
            while j>=0 and Array[j]>key:
                Array[j+1] = Array[j]
                j = j-1
            Array[j+1]=key
        return Array
    
    elif Set == False:
        for i in range(1,len(Array)):
            key = Array[i]
            """Insert Array[i] into the sorted subarray Array[1:i-1]"""
            j = i-1
            while j>=0 and Array[j]<key:
                Array[j+1] = Array[j]
                j = j-1
            Array[j+1]=key
        return Array
    else: 
        return TypeError("Set parameter should be a boolean value")

