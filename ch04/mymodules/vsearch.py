def search_for_vowels(phrase: str) -> set:
    """指定された単語内の母音を返す。"""
    return search_for_letters(phrase, "aeiou")


def search_for_letters(phrase: str, letters: str) -> set:
    """phrase内のlettersの集合を返す。"""
    return set(letters).intersection(set(phrase))
