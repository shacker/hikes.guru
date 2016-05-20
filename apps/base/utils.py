
def meters_to_dist(meters, pref, format="long"):
    '''
    Takes args `meters` (int) and `pref` ('mi' or 'km') and `type` ("short" or "long")
    If type=="short" returns float value in feet or meters.
    If type=="long" returns float value in miles or kilometers.
    '''

    if meters:
        print("have meters")
        if pref == "km" and format == "short":
            return meters  # meters
        elif pref == "km" and format == "long":
            return meters / 1000.0  # km
        elif pref == "mi" and format == "short":
            return meters * 3.28084  # feet
        else:
            # pref == "mi" and format == "long":
            return meters / 1609.344  # miles
    else:
        return None
