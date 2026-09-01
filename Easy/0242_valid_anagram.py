class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # Anagrams must be the same length — quick early exit
        # if they're not, no need to do any real work
        if len(s) != len(t):
            return False

        # Dictionary to count how many times each letter
        # appears in s
        s_dict = {}

        for i in s:
            if i in s_dict:
                s_dict[i] = s_dict[i] + 1
            else:
                s_dict[i] = 1

        # Now walk through t and "cancel out" letters from
        # the counts we built from s
        for i in t:
            if i in s_dict:
                # If this letter's count is already at 0,
                # t has more of this letter than s did —
                # not an anagram
                if s_dict[i] == 0:
                    return False
                s_dict[i] = s_dict[i] - 1
            else:
                # t has a letter that never appeared in s at all
                return False

        # Every letter in t matched and cancelled out a letter
        # from s with none left over — same letters, same counts
        return True
