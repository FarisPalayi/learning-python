def find_max(num_list):
  biggest_num = num_list[0]

  for number in num_list:
    if number > biggest_num:
      biggest_num = number

  return biggest_num