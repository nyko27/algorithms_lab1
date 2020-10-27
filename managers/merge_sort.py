class MergeSorter:
    comparison_count = 0
    swap_count = 0

    @staticmethod
    def sort_by_animals_count_descending(list_of_objects):
        MergeSorter.comparison_count = 0
        MergeSorter.swap_count = 0
        MergeSorter.merge_sort(list_of_objects)

    @staticmethod
    def merge_sort(list_of_objects):
        if len(list_of_objects) == 1:
            MergeSorter.comparison_count += 1
            return list_of_objects

        center = len(list_of_objects) // 2
        left_part = list_of_objects[:center]
        right_part = list_of_objects[center:]
        MergeSorter.merge_sort(left_part)
        MergeSorter.merge_sort(right_part)
        MergeSorter.merge(list_of_objects, left_part, right_part)

    @staticmethod
    def merge(arr, left_sub_array, right_sub_array):

        left_element = 0
        right_element = 0
        sorted_element = 0

        while left_element < len(left_sub_array) and right_element < len(right_sub_array):
            MergeSorter.comparison_count += 1
            if left_sub_array[left_element].number_of_animals > right_sub_array[right_element].number_of_animals:
                MergeSorter.comparison_count += 1
                arr[sorted_element] = left_sub_array[left_element]
                left_element += 1
            else:
                MergeSorter.comparison_count += 1
                arr[sorted_element] = right_sub_array[right_element]
                right_element += 1
            sorted_element += 1

        while left_element < len(left_sub_array):
            arr[sorted_element] = left_sub_array[left_element]
            left_element += 1
            sorted_element += 1

        while right_element < len(right_sub_array):
            arr[sorted_element] = right_sub_array[right_element]
            right_element += 1
            sorted_element += 1