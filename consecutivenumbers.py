# consecutive number function - loops through and adds the sum of consecutive values
def consecutive_numbers(lists):
    for a in range(len(lists)):
        try:
            lists[a] = int(lists[a])
        except ValueError:
            return "Please provide a list of numbers"
    if len(lists) <= 1:
            return "There should be more than one number"
    new_list = []
    counter = 1
    sum = 0
    for i in range(len(lists)):
        if i == len(lists)- 1 and sum != 0:
            if sum == lists[i]:
                new_list.append(lists[i] * counter) 
                break
            else:
                new_list.append(sum * counter)
                new_list.append(lists[i])
        elif i == len(lists)- 1:
            new_list.append(lists[i])
            break
        else:
            if lists[i+1] == lists[i]:
                counter += 1
                sum = lists[i]
            elif sum != 0:
                new_list.append(lists[i] * counter)
                counter = 1
                sum = 0
            else:
                new_list.append(lists[i])
    return new_list

# main code to test the function
if __name__=="__main__":
    while True:
        values = input("Please provide a list of numbers separated by commas that have some values that repeat consecutively: ")
        if values != "":
            break
    values_list = values.split(',')
    nums = []
    for i in range(len(values_list)):
        nums.append(values_list[i])

    print(consecutive_numbers(nums))