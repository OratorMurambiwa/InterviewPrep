# Last updated: 19/01/2026, 12:04:32
1class Solution(object):
2    def threeSumMulti(self, arr, target):
3        """
4        :type arr: List[int]
5        :type target: int
6        :rtype: int
7        """
8        MOD = (10 ** 9) + 7
9        count = Counter(arr)
10        keys = sorted(count.keys())
11        n = len(keys)
12        ans = 0
13
14        for i in range(n):
15            a = keys[i]
16
17            for j in range(i, n):
18                b = keys[j]
19
20                c = target - a - b
21
22                if c < b:
23                    continue
24
25                if c not in count:
26                    continue
27                
28                ca, cb, cc = count[a], count[b], count[c]
29
30                if a == b == c:
31                    if ca >= 3:
32                        ans += (ca * (ca-1) * (ca-2)) // 6
33                
34                elif a == b != c:
35                    if ca >=2:
36                        ans += (ca* (ca-1) //2 ) * cc
37
38                elif a != b == c:
39                    if cb >= 2:
40                        ans += ca * (cb * (cb-1)//2)
41
42                else:
43                    ans += ca * cb * cc
44
45                ans %= MOD
46        return ans
47
48                
49
50                
51        