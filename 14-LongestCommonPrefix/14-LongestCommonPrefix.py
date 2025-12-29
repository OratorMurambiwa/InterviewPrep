# Last updated: 29/12/2025, 03:04:13
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if strs is None:
            return ""

        prefix = strs[0]

        for word in strs[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]

                if prefix == "":
                    return ""
        return prefix

        