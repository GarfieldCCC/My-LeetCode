# 给定两个字符串 s 和 t，它们只包含小写字母。
#
#  字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。
#
#  请找出在 t 中被添加的字母。
#
#
#
#  示例 1：
#
#  输入：s = "abcd", t = "abcde"
# 输出："e"
# 解释：'e' 是那个被添加的字母。
#
#
#  示例 2：
#
#  输入：s = "", t = "y"
# 输出："y"
#
#
#  示例 3：
#
#  输入：s = "a", t = "aa"
# 输出："a"
#
#
#  示例 4：
#
#  输入：s = "ae", t = "aea"
# 输出："a"
#
#
#
#
#  提示：
#
#
#  0 <= s.length <= 1000
#  t.length == s.length + 1
#  s 和 t 只包含小写字母
#
#  Related Topics 位运算 哈希表
#  👍 249 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        big = s if s.__len__() > t.__len__() else t
        small = s if s.__len__() < t.__len__() else t
        s = "".join(sorted(list(small)))
        t = "".join(sorted(list(big)))
        for i in range(s.__len__() + 1):
            if s[0:i] != t[0:i]:
                return t[i - 1]
        return t[-1]
# leetcode submit region end(Prohibit modification and deletion)
