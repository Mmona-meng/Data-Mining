def all_itemsets(items, N):
    '''
    Generates all possible unique itemsets of size N from a given list of items.
    '''
    if N == 0:
        return [[]]
    if N > len(items):
        return []

    result = []
    for i in range(len(items)):
        # Generate all combinations that include the current item
        for subset in all_itemsets(items[i+1:], N-1):
            result.append([items[i]] + subset)

    return result


# Test the function with the provided example
test_items = ["ham", "cheese", "bread"]
test_result = all_itemsets(test_items, 2)
print(test_result)
