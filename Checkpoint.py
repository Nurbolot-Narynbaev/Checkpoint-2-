"""task 1"""
# words = ['bin', 'wheel', 'shadow']
# lengths = [len(word) for word in words]
# print(lengths)

"""task 2"""

# def convert_seconds_to_hms(time_list):
#     hms_list = []
#     for time in time_list:
#         hours = time // 3600
#         minutes = (time % 3600) // 60
#         seconds = (time % 3600) % 60
#         hms_list.append(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
#     return hms_list

# seconds= [120,543,666]

# print(convert_seconds_to_hms(seconds))

"""task 3"""
def square_list(lst):
    return list(map(lambda x: x**2, lst))

print(square_list([2, 55, 876]))
   git