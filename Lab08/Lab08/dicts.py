'''
Practice exercises on dict containers.
'''

from typing import Dict, List, Any

def get_frequencies(data: List[Any]) -> Dict[Any, int]:
    '''
    Count how often each item occurs.
    In:
        data - a list of items
    Out:
        return a dictionary: keys are items, values are # of times item occurs
    '''

    # Create a dictionary counts
    counts = {}

    # Loop, to visit each item in data
    for sample in data:
        if sample not in counts.keys():
            # Not in the dict already?
            counts.update({sample:0})
        # Increment Counter
        counts[sample] += 1

    #    In the loop, basically do counts[x] += 1
    #    but this will fail if counts[x] doesn't yet exist,
    #    so check first: if x in counts
    return counts

def has_duplicates(data: List[Any]) -> bool:
    '''
    Returns True/False if data has/hasn't repeated items
    '''

    # Call get_frequencies to count the items
    countsDict = get_frequencies(data)
    # Use for-loop to visit all the keys:
    # for x in counts:
    duplicates = False              # set duplicate var
    for key in countsDict.keys():
        if countsDict[key] > 1:     # greater than 1
            return False            # there are duplicates (break func)
    return True                     # return False otherwise
     
    #   any count that is > 1 means there are duplicates
    

def get_mode(data: List[Any]) -> Any:
    '''
    Get a the item that occurs MOST frequently.
    In:
        data - a list of items
    Out:
        return the most frequent item
    '''

    # Call get_frequencies to count the items
    countsDict = get_frequencies(data)

    # You're looking for the biggest count, so
    # initialize a 'biggest_count' to a small value, like 0.
    largestVal = 0
    largestKey = None

    # Use a for-loop to visit all the keys AND the values:
    # for x, count in counts.items()
    #   the 'items()' method visits all the key,value pairs
    #   if the count is bigger, update biggest_count, and mode too
    for key,val in countsDict.items():
        if val > largestVal:            # bigger than current value
            largestVal = val            # set new value
            largestKey = key            # corresponding key
    return largestKey

def is_invertible(dictionary: Dict[Any, Any]) -> bool:
    '''
    Returns True/False if the dictionary can/can't be inverted.
    A dictionary is invertible if every key maps to a different
    value.  So, if you get all the values in the dictionary,
    and there are duplicates, it can't be inverted.
    '''
    # make LIST of all values in dict:
    values = [i for i in dictionary.values()]

    # dictionary.values() is a list of values.  Call has_duplicates on it.
    return has_duplicates(values)

def inverted(dictionary: Dict[Any, Any]) -> Dict[Any, Any]:
    '''
    Invert a dictionary.
    In:
       dictionary: a dict
    Out:
       return a new dict, which is the inverse
    '''

    # Make a new dictionary, the inverse
    newDict = {}
    for key,val in dictionary.items():
        newDict.update({val:key})

    # run a for-loop to visit all the key,value pairs (see get_mode)
    # add each value,key pair to the inverse.
    return newDict 

def main():
    vals: List[int] = [1, 2, 3, 4, 5, 4, 2, 1, 2, 3, 4, 5, 6]
    print('counts   :', get_frequencies(vals))

    print('has dupes:', has_duplicates(vals))

    print('mode     :', get_mode(vals))

    num_names: Dict[str, int]\
        = {'one':1, 'two':2, 'five':5, 'three':3, 'four':4, 'a':1}
    unique_names: Dict[str, int]\
        = {'one':1, 'two':2, 'five':5, 'three':3, 'four':4}

    if is_invertible(num_names):
        print('num_names is invertible')
    else:
        print('num_names is not invertible')
    if is_invertible(unique_names):
        print('unique_names is invertible')
    else:
        print('unique_names is not invertible')

    print('inverted(num):', inverted(num_names))
    print('inverted(uniq):', inverted(unique_names))

if __name__ == '__main__':
    main()

