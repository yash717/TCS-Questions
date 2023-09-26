def NthRoot(n: int, m: int) -> int:
    if m == 0:
        # Handle the special case where 'm' is 0. The result is always 0 for any positive 'n'.
        return 0

    low = 1  # Initialize the lower bound of the search range.
    high = m  # Initialize the upper bound of the search range.

    while low <= high:
        # Calculate the middle value of the search range.
        mid = low + (high - low) // 2

        mid_power = mid ** n  # Calculate the 'nth' power of the middle value.

        if mid_power == m:
            # If the 'nth' power is equal to 'm', we found the 'nth' root, so return 'mid'.
            return mid
        elif mid_power < m:
            # If 'mid_power' is less than 'm', search in the higher range (move 'low' up).
            low = mid + 1
        else:
            # If 'mid_power' is greater than 'm', search in the lower range (move 'high' down).
            high = mid - 1

    # If we exit the loop without finding a result, return -1 to indicate no integer 'x' such that 'x^n = m'.
    return -1
