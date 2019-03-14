"""""""""""""""""""""

Configuration Options

"""""""""""""""""""""

# Label for value that represents no matches found
SIGNAL_NO: int = -1

# The number of spaces to add to the output of the visualization of KMP searching
VISUAL_OUTPUT_INDENT: int = 3

TEST_CASES: dict = {
    'A': {
        'pattern': 'ACACAGT',
        'text': 'ACAT ACGACACAGT'
    },
    'B': {
        'pattern': 'ABABAAAABBBBAABABABAAAA',
        'text': 'AABABABABABBBBBBAAABBABAAABBBAABBABAAABABBABABAAAABBBBAABABABAAAABBAABABBABABAB'
    },
    'Matt': {
        'pattern': 'Matt',
        'text': 'Hello, my name is Matt, and this is a test case.'
    },
    'Rat': {
        'pattern': 'rat and the cat, Matt, rat and the cat',
        'text': 'There was a rat and the cat, Matt, rat and the rat and the cat, Matt did not like the hat. rat and '
                'the cat, Matt, rat and the cat.'
    }
}

# The pattern / text combo(s) to test, accepts multiple cases
USE_TEST_CASES_INDEX: set = {'A'}
# USE_TEST_CASES_INDEX: set = TEST_CASES.keys()

"""""""""""""""""""""""

Algorithms Implemented

"""""""""""""""""""""""


def z_array(pattern: str, text: str) -> list:
    """
    The method that computes a z-array that has the length of the longest prefixes of itself in a concatenated pattern & 
    string (P$T).
    
    :param pattern: The pattern to check in the text
    :param text: The text to check if the pattern is within
    :return: The z-array with the count of the largest prefix starting at each index of P$T
    """
    full_text = pattern + "$" + text

    z = ['X']

    # Each position of the z array to calculate
    for k in range(1, len(full_text)):

        # The length of the substring to check
        j = 0

        # While within bounds of the full text and the substring contains the beginning of P$T
        while j < len(full_text[k:]) and full_text.startswith(full_text[k:k + j + 1]):

            # See if a substring matches that is 1 char longer
            j += 1

        # Populate the z array with the length of the longest substring that is a prefix of the full text at each index
        z.append(j)

    return z


def kmp_prefix(pattern: str) -> list:
    """
    Calculates the prefix table for use in the KMP search algorithm.

    :param pattern: The pattern to calculate prefixing on
    :return: The prefix table (KMP)
    """
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


def kmp_search(pattern: str, text: str, prefixes: list = list(), visualize=False) -> int:
    """
    The searching algorithm that implements KMP searching technique. This is similar to the naive method, but when a
    mismatch is found, it checks the prefix table to see how many positions it can skip in the text. This can result
    in a lower time complexity compared to the naive search method, which can help when searching highly repetitive data
    for information like that of DNA sequences.

    :param pattern: The pattern to search the text for
    :param text: The text that is being searched in
    :param prefixes: The prefix table with the counts of positions that can be skipped for any given mismatch location
    :param visualize: Whether or not to show the steps the algorithm used and how many locations were skipped. (off by
    default)
    :return: Returns SIGNAL_NO (default = -1) if the text doesn't contain the pattern, or the index of the pattern in
    the text, if the text does contain the pattern
    """
    # If no prefix table is specified, build one automatically
    if len(prefixes) == 0:
        prefixes = kmp_prefix(pattern=pattern)

    if len(prefixes) != len(pattern):
        raise ValueError('The length of the pattern does not match the length of the prefix table!')

    # Calculate indentation from global setting
    indent = ' ' * VISUAL_OUTPUT_INDENT

    # The index of the start of the substring being compared in the text
    i = -1

    if visualize:
        skip_count = 0

    while i < len(text) - len(pattern):
        i += 1

        if visualize:
            print(indent + text)

            print(indent + ' ' * i + pattern)

        # The offset from i / location of the char in the prefix list
        j = -1

        # The location of the mismatch in the pattern and substring (SIGNAL_NO is no mismatch found yet)
        mismatch = SIGNAL_NO

        while mismatch == SIGNAL_NO and j < len(pattern) - 1 and i + j < len(text) - len(pattern):
            j += 1

            # If there is a mismatch
            if text[i + j:i + j + 1] != pattern[j:j + 1]:

                # Take note of the location of the mismatch
                mismatch = j

                if visualize:
                    skip_count += prefixes[mismatch]
                    print(indent + 'Mismatch at index ' + str(mismatch) + ' of pattern, skipping ' + str(prefixes[mismatch]) + ' locations')

        # If the text matched the pattern
        if mismatch == SIGNAL_NO:

            if visualize:
                print(indent + 'Pattern found starting at index ' + str(i) + ' in the text!\n')
                print(indent + 'Skipped ' + str(skip_count) + ' locations total.')

            # Return the location of the start of the match in the text
            return i

        # Skip the number of positions according to the prefix table
        i += prefixes[mismatch]

    if visualize:
        print(indent + 'Pattern not found in the text!')


"""""""""""""""""

Assignment Output

"""""""""""""""""


class Main:

    for case in USE_TEST_CASES_INDEX:

        pattern = TEST_CASES[case]['pattern']
        text = TEST_CASES[case]['text']

        print('\nGiven:')
        print('   Pattern: ' + pattern)
        print('   Text: ' + text)

        print('\nZ Algorithm:\n')

        """
        1. Z array of the string P$T
        """

        z = z_array(pattern=pattern, text=text)
        print('1. Z-Array = ' + str(z))

        """
        2. Whether or not this pattern is present in the text (Yes/No)
        """

        if len(pattern) not in z:
            print('2. Present = No')
        else:
            print('2. Present = Yes')

            """
            3. The beginning index within the text at which the pattern matches (If the pattern is present). This is not the 
            beginning index of the concatenated P$T string. This is the beginning index within T. Assume that index counting starts 
            at 0.
            """

            print('3. Beginning Index = ' + str(z.index(len(pattern)) - (len(pattern) + 1)))

        """
        For KMP, output the following:
        """

        print('\nKMP Algorithm:\n')

        """
        1. The prefix table
        """

        p = kmp_prefix(pattern=pattern)
        print('1. Prefix Table = ' + str(p))

        """
        2. Whether or not this pattern is present in the text (Yes/No)
        """

        kmp_match_index = kmp_search(pattern=pattern, text=text, prefixes=p)
        if kmp_match_index == SIGNAL_NO:
            print('2. Present = No')
        else:
            print('2. Present = Yes')

            """
            3. The beginning index within the text at which the pattern matches (If the pattern is present).  Assume that index 
            counting starts at 0.
            """

            print('3. Beginning Index = ' + str(kmp_match_index))

        """
        4. If you wish, you can output a step by step visual analysis of how the pattern shifts under the text.
        """

        print('4. Visualization of search...\n')
        kmp_search(pattern=pattern, text=text, prefixes=p, visualize=True)
