def z_algorithm(pattern: str, text: str) -> list:
    full_text = pattern + "$" + text

    z = ['X']

    # Each position of the z array to calculate
    for k in range(1, len(full_text)):

        # The length of the substring to check
        j = 0

        # While within bounds of the full text
        while j < len(full_text[k:]) and full_text.startswith(full_text[k:k + j + 1]):

            # See if a substring matches that is 1 char longer
            j += 1

        # Populate the z array with the length of the longest substring that is a prefix of the full text at each index
        z.append(j)

    return z


"""
Determine if the following pattern occurs in the following text:

"""
pattern = 'ACACAGT'

text = 'ACAT ACGACACAGT'

"""
Use the Z algorithm and KMP for this assignment.

For the Z algorithm, output the following:
"""

z = z_algorithm(pattern=pattern, text=text)

"""
1. Z array of the string P$T
"""

print('1. ' + str(z))

"""
2. Whether or not this pattern is present in the text (Yes/No)
"""

if len(pattern) in z:
    print('2. Yes')
else:
    print('2. No')

"""
3. The beginning index within the text at which the pattern matches (If the pattern is present). This is not the 
beginning index of the concatenated P$T string. This is the beginning index within T. Assume that index counting starts 
at 0.
"""

print('3. ' + str(z.index(len(pattern)) - (len(pattern) + 1)))

"""
For KMP, output the following:
"""

# TODO: Calculate prefix table

"""
1. The prefix table
"""

# TODO: 1. The prefix table

"""
2. Whether or not this pattern is present in the text (Yes/No)
"""

# TODO: 2. Whether or not this pattern is present in the text (Yes/No)

"""
3. The beginning index within the text at which the pattern matches (If the pattern is present).  Assume that index 
counting starts at 0.
"""

# TODO: 3. The beginning index within the text at which the pattern matches (If the pattern is present).

"""
4. If you wish, you can output a step by step visual analysis of how the pattern shifts under the text.
"""
