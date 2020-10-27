from managers.swap import swap_elements


class InsertionSorter:
    comparison_count = 0
    swap_count = 0

    @staticmethod
    def insertion_sort_by_attendance_per_year_ascending(list_of_objects):
        InsertionSorter.swap_count = 0
        InsertionSorter.comparison_count = 0

        for current_element_index in range(1, len(list_of_objects)):
            edge_element = list_of_objects[current_element_index]
            sorted_element_index = current_element_index - 1
            while edge_element.attendance_per_year < list_of_objects[sorted_element_index].attendance_per_year and sorted_element_index >= 0:
                InsertionSorter.comparison_count += 2
                swap_elements(list_of_objects, sorted_element_index + 1, sorted_element_index)
                InsertionSorter.swap_count += 1
                sorted_element_index -= 1

