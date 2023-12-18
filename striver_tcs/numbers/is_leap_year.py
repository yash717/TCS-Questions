def is_leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return "Yes"
    else:
        return "No"


# Test cases
year1 = 1996
print(f"Input: {year1}")
print(f"Output: {is_leap_year(year1)}")
# Output: Yes

year2 = 2000
print(f"\nInput: {year2}")
print(f"Output: {is_leap_year(year2)}")
# Output: Yes
