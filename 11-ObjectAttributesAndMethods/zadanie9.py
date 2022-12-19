import random

class Arrays():

    @staticmethod
    def method_first(number_of_array_elements, value_of_array_elements):
        arr = []
        for i in range(number_of_array_elements):
            arr.append(value_of_array_elements)
        return arr

    @staticmethod
    def method_second(number_of_array_elements, value_from, value_to):
        arr = []
        for i in range(number_of_array_elements):
            random_number = random.randint(value_from,value_to)
            arr.append(random_number)
        return arr 

    @staticmethod
    def method_third(array, value_from, value_to):
        counter = 0
        for i in range(len(array)):
            if array[i] >= value_from and array[i] <= value_to:
                counter += 1
        return counter     

print(Arrays.method_first(5,5))           
print(Arrays.method_second(5,5,10))
print(Arrays.method_third([5,6,7,8,9,11],5,10))
