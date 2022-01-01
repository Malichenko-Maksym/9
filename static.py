class Arrays():
    @staticmethod
    def print_in_col(array):
        for c in array:
            print(c)
    def print_in_row(array):
        for c in range(len(array)):
            if c!=len(array)-1:
                print(f"{array[c]},",end="")
            else: print(array[c])
    def same(number_of_elements, value_of_elements):
        a=[]
        for i in range(number_of_elements):
            a.append(value_of_elements)
        return a
    def cr_random(number,down,up):
        import random
        a=[]
        for i in range(number):
            a.append(random.randint(down,up))
        return a
    def number_of_range(array, value_from, value_to):
        s=0
        for i in array:
            if i<=value_to and i>=value_from: s+=1
        return s

        
my_array = [4,1,8,7,2]
print(Arrays.number_of_range(my_array,2,8))
