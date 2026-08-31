class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        # Edge case: no words at all — return a list containing
        # one empty group
        if not strs:
            return [[""]]

        # Final result: a list of groups, each group is a list
        # of words that are anagrams of each other
        result = []

        # Maps canonical form (sorted letters) -> list of
        # original words that match that form
        groups = {}

        for word in strs:
            # Sorting the letters gives a form that's identical
            # for all anagrams of each other, e.g. "eat" and "tea"
            # both become "aet"
            key = "".join(sorted(word))

            if key in groups:
                # Seen this canonical form before — add this word
                # to the existing group, in place (no copying)
                groups[key].append(word)
            else:
                # First word with this canonical form — start a
                # new group
                groups[key] = [word]

        # Pull out just the groups themselves, not the keys
        for key in groups:
            result.append(groups[key])

        return result
