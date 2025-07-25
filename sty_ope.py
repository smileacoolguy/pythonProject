str_1="Test1234abd"

result_str=""
for f in str_1:
    if f.isdigit():
        # print(f)
        result_str+=f
print(result_str)