def alphabet_position(text):
    nums = [str(ord(a) - 96) for a in text.lower() if a.isalpha()]
    #The Python ord() method converts a character into its Unicode code.
    # then substract 96 from a position in ASCII as the first letter a == 97
    # isalpha checks whether letter in alphabet or not
    return " ".join(nums)
    # convert all elements in a list to a one string
print(alphabet_position("Hello how are you"))
