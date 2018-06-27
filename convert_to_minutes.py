def convert_to_minutes(num_hours):
    '''(int) -> int

    Return the number of minutes there are in num_hours hours.
    >>>convert_to_minutes(2)
    120
    '''
    result = num_hours * 60
    return result

minutes_2 = convert_to_minutes(2)
minutes_3 = convert_to_minutes(3)
