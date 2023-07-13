def concatenateData(tuple1, tuple2):
    concatenated_tuple = tuple1 + tuple2
    first_data1 = concatenated_tuple[0]
    first_data2 = concatenated_tuple[len(tuple1)]

    print([(first_data1, first_data2)])

concatenateData((1, 2, 3), (4, 5, 6))