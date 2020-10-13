from managers.merge_sort import MergeSorter
from managers.insertion_sort import InsertionSorter
from models.zoo import Zoo
import csv
import time

if __name__ == '__main__':

    list_of_zoos = []
    with open('data.csv', 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)

        for line in csv_reader:
            list_of_zoos.append(Zoo(name=line[0], number_of_animals=int(line[1]) % 1000,
                                    attendance_per_year=int(line[2]) // 10000))


    print('\n\nZoos sorted with a merge method by animals count in descending way:\n')
    time_before_merge_sort = time.time()
    MergeSorter.sort_by_animals_count_descending(list_of_zoos)
    time_after_merge_sort = time.time()
    merge_sorting_time = time_after_merge_sort - time_before_merge_sort

    for zoo in list_of_zoos:
        print(str(zoo))

    print(f'\nTime taken for merge sorting: {merge_sorting_time}seconds ')
    print(f'Amount of swaps : {MergeSorter.swap_count}')
    print(f'Amount of comparisons: {MergeSorter.comparison_count}\n\n\n')

    print('Zoos sorted with an insertion method by increasing number of visitors:\n')
    time_before_insertion_sort = time.time()
    InsertionSorter.insertion_sort_by_attendance_per_year_ascending(list_of_zoos)
    time_after_insertion_sort = time.time()
    insertion_sort_time = time_after_insertion_sort - time_before_insertion_sort

    for zoo in list_of_zoos:
        print(str(zoo))

    print(f'\nTime taken for insertion sorting: {insertion_sort_time} seconds')
    print(f'Amount of swaps : {InsertionSorter.swap_count}')
    print(f'Amount of comparisons: {InsertionSorter.comparison_count}')
