
def my_Levenshtein(string1, string2):
    if len(string1) == len(string2): # check if length of both parameters is same
        if string1 == string2: 
            #if both parameters are identical/same size then return 0
            return 0
        else:
            diff = 0 # To store the difference
            for i in range(len(string1)): # Iterate through each character in string
                if string1[i] != string2[i]: 
                    # if character in string1 is different from character in string2
                    # then count the difference as 1
                    diff = diff + 1 
            return diff # return the difference
    else:
        return -1 # if length is not same then return -1




if __name__ == "__main__":
    val = my_Levenshtein("GGACTAB","GGACTGA")
    print(val)