import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quick_sort(low: int, high: int):
            if low >= high:
                return

            # Random pivot selection to prevent worst-case TLE
            pivot_idx = random.randint(low, high)
            nums[low], nums[pivot_idx] = nums[pivot_idx], nums[low]
            pivot = nums[low]

            # 3-Way Partitioning (< pivot, == pivot, > pivot)
            lt = low      # nums[low..lt-1] < pivot
            i = low + 1   # nums[lt..i-1] == pivot
            gt = high     # nums[gt+1..high] > pivot

            while i <= gt:
                if nums[i] < pivot:
                    nums[lt], nums[i] = nums[i], nums[lt]
                    lt += 1
                    i += 1
                elif nums[i] > pivot:
                    nums[i], nums[gt] = nums[gt], nums[i]
                    gt -= 1
                else:
                    i += 1

            quick_sort(low, lt - 1)
            quick_sort(gt + 1, high)

        quick_sort(0, len(nums) - 1)
        return nums