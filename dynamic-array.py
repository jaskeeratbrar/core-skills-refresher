class DynamicArray:
    
    # Initialize array
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.arr = [0] * capacity

    # Get the value of i-th index
    def get(self, i: int) -> int:
        return self.arr[i]

    # Assign value of 'n' to i-th index
    def set(self, i: int, n: int) -> None:
        self.arr[i] = n


    # Assign value at the end of array
    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        
        self.array[self.length] = n
        self.length += 1


    def popback(self) -> int:
        if self.size > 0

            self.length -= 1
        
        return self.array[self.length]

 
    # Increase the size of array
    def resize(self) -> None:

        # Initialize an empty array, assign its capacity double of our original array
        self.capacity = 2 * self.capacity
        new_arr = [0] * self.capacity

        # Copy elements from old array to new
        for i in range(self.length):
            new_arr[i] = self.arr[i]

        # Replace original array with the new array     
        self.arr = new_arr

    # Return the number of elements stored in the array
    def getSize(self) -> int:
        return self.length
        
    
    def getCapacity(self) -> int:
        return self.capacity
