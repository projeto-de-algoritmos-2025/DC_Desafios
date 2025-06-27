class Solution:
    def goodTriplets(self, nums1: list[int], nums2: list[int]) -> int:
        n = len(nums1)
        if n < 3:
            return 0

        pos2 = [0] * n
        for i in range(n):
            pos2[nums2[i]] = i
        
        p = [0] * n
        for i in range(n):
            p[i] = pos2[nums1[i]]

        less_left = [0] * n
        greater_right = [0] * n
        
        items = [(p[i], i) for i in range(n)]

        def divide_and_conquer(enum_items):
            m = len(enum_items)
            if m <= 1:
                return enum_items

            mid = m // 2
            left_half = divide_and_conquer(enum_items[:mid])
            right_half = divide_and_conquer(enum_items[mid:])
            
            j = 0
            for i in range(len(left_half)):
                while j < len(right_half) and right_half[j][0] < left_half[i][0]:
                    j += 1
                original_index = left_half[i][1]
                greater_right[original_index] += len(right_half) - j

            j = 0
            for i in range(len(right_half)):
                while j < len(left_half) and left_half[j][0] < right_half[i][0]:
                    j += 1
                original_index = right_half[i][1]
                less_left[original_index] += j
            
            merged = []
            l_ptr, r_ptr = 0, 0
            while l_ptr < len(left_half) and r_ptr < len(right_half):
                if left_half[l_ptr][0] < right_half[r_ptr][0]:
                    merged.append(left_half[l_ptr])
                    l_ptr += 1
                else:
                    merged.append(right_half[r_ptr])
                    r_ptr += 1
            merged.extend(left_half[l_ptr:])
            merged.extend(right_half[r_ptr:])
            
            return merged

        divide_and_conquer(items)

        total_triplets = 0
        for i in range(n):
            total_triplets += less_left[i] * greater_right[i]
            
        return total_triplets