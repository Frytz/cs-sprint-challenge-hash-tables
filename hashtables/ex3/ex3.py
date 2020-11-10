def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    #create dict
    int_dict= {}
    #create array
    result = []
    #loop through the array and add to the dict, increment in there is a dup
    for i in arrays:
        for j in i:
            if j not in int_dict:
                int_dict[j] = 1
            else:
                int_dict[j] += 1
                if int_dict[j] == len(arrays):
                    result.append(j)
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
