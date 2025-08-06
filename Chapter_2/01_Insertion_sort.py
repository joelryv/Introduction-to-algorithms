def insertion_sort(arr):
    """
    Perform insertion sort on the given list.

    :param arr: List of elements to be sorted
    :return: Sorted list
    """
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1        
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key
    
    return arr

import unittest

class TestInsertionSort(unittest.TestCase):
    def test_insertion_sort(self):
        self.assertEqual(insertion_sort([5, 2, 9, 1, 5, 6]), [1, 2, 5, 5, 6, 9])
        self.assertEqual(insertion_sort([3, 0, -2, 8, -1]), [-2, -1, 0, 3, 8])
        self.assertEqual(insertion_sort([]), [])
        self.assertEqual(insertion_sort([1]), [1])
        self.assertEqual(insertion_sort([4, 3, 2, 1]), [1, 2, 3, 4])
    def test_insertion_sort_with_duplicates(self):
        self.assertEqual(insertion_sort([3, 3, 2, 1, 2]), [1, 2, 2, 3, 3])
        self.assertEqual(insertion_sort([5, 5, 5]), [5, 5, 5])

if __name__ == "__main__":
    unittest.main()