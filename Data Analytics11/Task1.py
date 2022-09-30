def int_to_Roman(num):
    val = [1000, 900, 500, 400,100, 90, 50, 40,10, 9, 5, 4,1]
    # All digits
    syb = ["M", "CM", "D", "CD","C", "XC", "L", "XL","X", "IX", "V", "IV","I"]
    # Roman numbers of the digits

    roman_num = '' # To store the roman number
    i = 0  # Start from the first position in digits list
    while  num > 0:  # Loop through the list until given number is less than 0
        for j in range(num // val[i]): # Loop through the list of digits
            roman_num += syb[i] # append the particular roman symbol to the roman digit
            num -= val[i] # subtract the particular number of list from given number
        i += 1 # increment the position in digits list
    return roman_num # return roman number


if __name__ == "__main__":
    print(int_to_Roman(2))
