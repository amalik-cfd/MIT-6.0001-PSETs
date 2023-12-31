# Problem Set 4A
# Name: Abdul Malik Huzaifa
# Collaborators: None
# Time Spent: 1 day

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    permlist = []
    if len(sequence) == 1:
         permlist.append(sequence)
         return permlist
     
        
    elif len(sequence) == 2:
        permlist.append(sequence)
        permlist.append(sequence[1]+sequence[0])
        return permlist
    
    
    else:
        s1 = sequence[0]
        s2 = sequence[1:]
        for n in get_permutations(s2):
            for i in range(len(n)+1):
                seqlist = list(n)
                seqlist.insert(i,s1)
                k =''.join(seqlist)
                permlist.append(k)
        return permlist

if __name__ == '__main__':
#    #EXAMPLE
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))

