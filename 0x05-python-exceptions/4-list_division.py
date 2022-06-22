#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_len):
    answer = []
    for index in range(list_length):
        try:
            result = my_list_1[list_len] / my_list_2[list_len]
        except IndexError:
            print ("out of range")
        except ZeroDivision:
            print ("division by 0"
        except TypeError:
            print ("wrong type")
	finally:
            answer.append(result)
    return (answer)
