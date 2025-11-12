# Guess Number Higher Or Lower
# https://neetcode.io/problems/guess-number-higher-or-lower?list=neetcode250
# Language: Python
# Difficulty: Unspecified


        while l <= r:
            m = (l+r)//2

            if guess(m) == 0:
                return m
            elif guess(m) < 0:
                r = m - 1
            else:
                l = m + 1
