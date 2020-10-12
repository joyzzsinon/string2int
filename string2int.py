def string_to_int(txt):
    result = 0
    number_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for idx_txt in txt:
        if idx_txt in number_list:
            result = result * 10
            for idx_num in number_list:
                if idx_txt > idx_num:
                    result = result + 1
    return result
