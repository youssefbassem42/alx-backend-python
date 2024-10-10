#!/usr/bin/env python3
''' sum list function '''

def sum_list(input_list : list[float]) -> float:
    ''' 
    Calculate the sum of a list of floating-point numbers.

    Parameters:
    input_list (list[float]): A list of floating-point numbers to be summed.

    Returns:
    float: The sum of the input list as a floating-point number.
    '''
    return float(sum(input_list))
