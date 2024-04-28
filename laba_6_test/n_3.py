import collections

def non_unique_chars(s: str) -> int:
    if type(s) != str:
        raise TypeError("s must be a string")
    if len(s) == 0:
        return 0
    else:
        res = collections.Counter(s)
        return sum(1 for i in res if res[i] > 1)


test_pairs = [
 ("", 0),
 ("lorem", 0),
 ("bunny", 1),
 ("aba", 1),
 ("abba",
2),
 ("abcd", 0),
 ("abcc", 1),
 ("ab", 0),
 ([111,2], None),
 ({34,2}, None),
(False, None),
 (True, None),
 (1, None),
 (0, None),
 (None, None),
 ((123124,
123123), None)
 ]

def test_non_unique_chars():
    for args, correct_res in test_pairs:
        try:
            res = non_unique_chars(args)
        except TypeError:
            if correct_res is None:
                continue

            print(f"Unexpected TypeError: {args} -> {correct_res}")
            assert False
           
        except Exception as err:
            print(f"Unexpected exception: {err}")
            assert False

        else:
            if res != correct_res:
                print(f"{args} -> {res} != {correct_res}")
                assert False
