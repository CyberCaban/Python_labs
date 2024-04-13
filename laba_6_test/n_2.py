def is_palindrome(s: str) -> bool:
    if type(s) != str:
        raise TypeError
    if len(s) < 3:
        raise ValueError
    if s == s[::-1]:
        return True
    else:
        return False


test_pairs = [
    ("", None),
    ("a", None),
    ("aa", None),
    ("aba", True),
    ("abba", True),
    ("abcd", False),
    ("abcc", True),
    ("ab", None),
    ([111,2], None),
    ({34,2}, None),
    (False, None),
    (True, None),
    (1, None),
    (0, None),
    (None, None),
    ((123124, 123123), None)
]

def test_palindrome():
    for args, correct_res in test_pairs:
        try:
            res = is_palindrome(args)
        except Exception as err:
            if correct_res is None:
                continue
            
            print(f"Unexpected {err}: {args} -> {correct_res}")
            assert False
        
        else:
            if res != correct_res:
                print(f"{args} -> {res} != {correct_res}")
                assert False