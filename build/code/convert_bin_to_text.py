# -*- coding: utf-8 -*-

import cPickle, copy

def convert():
    
    print '\nconvert .bin to .txt'
    
    src_data = '..\\output\\data_full_with_network.bin'
    
#    data .bin loaded from \output, not moved to \temp first
    
    print 'loading', src_data
    
    try:
        
        f = open(src_data, 'rb')
        data_hold = cPickle.load(f)
        f.close()

    except IOError:
    
        raise IOError('data unavailable', src_data)
  
    var_list = copy.deepcopy(data_hold[data_hold.keys()[0]].keys())
    
#    http://stackoverflow.com/questions/16581695/python-how-to-sort-lists-alphabetically-with-respect-to-capitalized-letters
    var_list = sorted(var_list, key=lambda L: (L.lower(), L))
    
    data_dict = {}
    
    for key in data_hold:
        
        data_dict[key] = []
        
        for var in var_list:
            
            try:            
            
                data_dict[key].append(data_hold[key][var])
                
            except KeyError:
                
                if var in ['B6', 'CO', 'HP', 'NW', 'SY', 'TZ', 'YX']:
                    
                    data_dict[key].append(0)
                    
                else:

                    print 'missing key', var, '(recorded as NA)'                    
                    data_dict[key].append('NA')
    
    output_string = ''
    
    dst_txt = '..\\output\\'+'data_full_with_network.txt'

    header_line = 'origin' + '\t' + 'dest' + '\t' + 'carrier' +\
        '\t' + 'year' + '\t' + 'quarter' + '\t'

    for i in var_list:
        
        header_line += str(i)
        header_line += '\t'
        
    header_line = header_line.rstrip()    
    header_line += '\n'

    output_string += header_line

    length_of_data = len(data_dict)
    step_length = length_of_data // 100

    count = 0
    
    for key in data_dict:
        
        if count % step_length == 0:
            
            print count // step_length, '%'
        
        data_line = key.split('_') + data_dict[key]
        
        for item in data_line:
            
            output_string += str(item)
            output_string += '\t'
            
        output_string = output_string.rstrip()
        output_string += '\n'
        
        count += 1        
        
    output_string = output_string.rstrip()

    print '\nsaving', dst_txt

    f = open(dst_txt, 'w')
    f.write(output_string)
    f.close()
    
    return None
