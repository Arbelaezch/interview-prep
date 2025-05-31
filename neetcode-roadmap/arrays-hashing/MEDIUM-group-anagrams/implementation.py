def groupAnagrams(strs):
    """
    Group anagrams together using sorted string as key.

    Args:
        strs: List of strings to group

    Returns:
        List of lists, where each inner list contains anagrams
    """

    grouped_anagrams = {}

    for word in strs:
        sorted_word = ''.join(sorted(word))

        if sorted_word not in grouped_anagrams:
            grouped_anagrams[sorted_word] = []

        grouped_anagrams[sorted_word].append(word)

    return list(grouped_anagrams.values)


    
