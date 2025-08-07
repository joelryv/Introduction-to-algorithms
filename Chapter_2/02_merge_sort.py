def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]        # Dividing the elements into 2 halves
        R = arr[mid:]

        merge_sort(L)  # Sorting the first half
        merge_sort(R)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return arr

import unittest
class TestMergeSort(unittest.TestCase):
    def test_merge_sort(self):
        self.assertEqual(merge_sort([5, 2, 9, 1, 5, 6]), [1, 2, 5, 5, 6, 9])
        self.assertEqual(merge_sort([3, 0, -2, 8, -1]), [-2, -1, 0, 3, 8])
        self.assertEqual(merge_sort([]), [])
        self.assertEqual(merge_sort([1]), [1])
        self.assertEqual(merge_sort([4, 3, 2, 1]), [1, 2, 3, 4])

    def test_merge_sort_with_duplicates(self):
        self.assertEqual(merge_sort([3, 3, 2, 1, 2]), [1, 2, 2, 3, 3])
        self.assertEqual(merge_sort([5, 5, 5]), [5, 5, 5])

if __name__ == "__main__":
    unittest.main()