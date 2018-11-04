from mldata import *
from test_mldata import *
from math import log2
import numpy as np
from IG_v5 import *

'''
This function is sample main funtion about using IG.py
All of the operation in Main() function should be added.
'''

def main():
    '''
    dataset operation
    '''
    data_read = parse_c45("example")
    data_array = np.array(data_read.to_float())
    # data_fil = filter_for_None(data_array)      #delete all None in array
    none_row, none_column = np.where(data_array == None)
    print(none_row,none_column)
    '''
    which column to choose
    '''
    i = 2
    print(data_read.schema[i].type)
    for x in none_column:
        if x == i:
            index = np.where(none_column == i)
            data_array = np.delete(data_array,none_row[index],0)
    print('---The available values array is ---\n',data_array)

    if data_read.schema[i].type == 'CONTINUOUS':
        print('flag1')
        data_arranged, value_ratio = continuous_data(data_array,i)
        #  print(data_arranged)
        # print(value_ratio)
        threshold, hyx = find_minima_threshold(value_ratio)
        print('threshold = ', threshold)
        print('H(Y|X) = ', hyx)

    else: 
        print('flag2')
        data_arranged,value_ratio = discrete_data(data_array,i)
        hyx = calculate_hyx(value_ratio)
        print('H(Y|X)=',hyx)
    ig = information_gain(data_array,hyx)
    print('InformationGain =',ig)
    g_ratio = gain_ratio(ig, value_ratio)
    print('GainRatio =', g_ratio)


if __name__ == '__main__':
    main()