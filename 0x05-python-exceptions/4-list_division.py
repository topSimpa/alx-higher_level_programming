#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_len):
    answer = []
    for index in range(list_len):
        try:
            result = my_list_1[index] / my_list_2[index]
        except IndexError:
            print("out of range")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except TypeError:
            print("wrong type")
            result = 0
        finally:
            answer.append(result)
    return (answer)
