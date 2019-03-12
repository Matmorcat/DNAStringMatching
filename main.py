def z_array(pattern: str, text: str) -> list:
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


def kmp_prefix(pattern: str) -> list:

    p = [0]

    # The last element of the suffix to check
    i = 0

    while i < len(pattern) - 1:
        i += 1

        pattern_slice = pattern[:i + 1]

        # The length of the suffix / prefix to compare
        j = 0

        # The length of the longest suffix and prefix in common for the substring (result of while loop on j)
        longest_common = 0

        # Continue until the last possible prefix and suffix
        while j < i - 1:
            j += 1

            if pattern_slice[:j] == pattern_slice[-1 * j:]:
                longest_common = j

        p.append(longest_common)

    return p


class Main:
    """
    Determine if the following pattern occurs in the following text:

    """
    pattern = 'ACACAGT'

    text = 'ACAT ACGACACAGT'

    """
    Use the Z algorithm and KMP for this assignment.
    
    For the Z algorithm, output the following:
    """

    print('\nZ Algorithm:\n')
    z = z_array(pattern=pattern, text=text)

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

    print('\nKMP Algorithm:\n')
    p = kmp_prefix(pattern=pattern)

    """
    1. The prefix table
    """

    print('\nKMP Algorithm:\n')
    print('1. ' + str(p))

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
