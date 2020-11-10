def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    #create dict
    weight_dict = {}

    for i, weight in enumerate(weights):
        #check for counter
        counter = limit - weight
        if counter in weight_dict:
            #check if counter or found key is larger
            if i >= weight_dict[counter]:
                return (i, weight_dict[counter], i)
            return (weight_dict[counter], i)
        #add new item
        weight_dict[weight] = i

    return None
