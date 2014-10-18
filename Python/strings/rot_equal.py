"""
Check if a string is rotationally equal to 
another
"""

def check_rot_equal(s1, s2):
    """
    Is s1 rotationally equal to s2?
    """
    if len(s1) != len(s2) or not s1 or not s2:
        return False

    if s1 == s2:
        return True

    s2 += s2
    return s2.count(s1) >= 1


print check_rot_equal("abcde", "cdeab")
print check_rot_equal("abcde", "deabc")
print check_rot_equal("abcde", "deab")
print check_rot_equal("abcde", "")
