class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return

        counter = 0
        p1 = 0
        p2 = 0
        m_current = m
        while p2 < n and p1 < m_current:
            if nums1[p1] > nums2[p2]:
                nums1.insert(p1, nums2[p2])
                p2 = p2 + 1
                p1 = p1 + 1
                m_current += 1
            else:
                p1 = p1 + 1
            counter = counter + 1
        
        while p2 < n:
            nums1.insert(p1, nums2[p2])
            p2 += 1
            p1 += 1

        while len(nums1) > (m + n):
            nums1.pop()