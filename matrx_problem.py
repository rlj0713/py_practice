import math

nums = open('matrix_test.txt', 'r+')
content = nums.read()
content_list = content.split(", ")

class Number:
    def __init__(self, row, column, value):
        self.row = row
        self.column = column
        self.value = value
    
j = 1
for i in content_list:
    row = math.floor(j / 5)
    column = math.floor(j / 5) or j % 5
    # globals() allows for a dynamic variable assignment
    globals()[f"value{j}"] = Number(column, row, content_list[j - 1])
    j += 1


#Format is 'value#'
def check_number(object_name):
    print("column", object_name.column, "row", object_name.row, object_name.value)

check_number(value1)
check_number(value5)
check_number(value8)
check_number(value25)