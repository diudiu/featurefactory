
import operator


def get_range_map_val(range_list, input_val):
    """
    [)  (]
    """
    mapping_val = None

    for item in range_list:
        range = item.get('range')
        if operator.ge(input_val, range[0]) and operator.le(input_val, range[1]):
            mapping_val = item.get('mapping_val')
            break

    return mapping_val
