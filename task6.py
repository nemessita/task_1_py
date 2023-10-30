# test_list = [5, 6, [], 3, [], [], 9]
# bos olanlari listden cix ve ededleri ekrana yazdir

# --------------------------------------------------
test_list = [5, 6, [], 3, [], [], 9]
non_empty_list = [item for item in test_list if item]
for item in non_empty_list:
    print(item)
# --------------------------------------------------
# test_list = [5, 6, [], 3, [], [], 9]
# newList = []
# for i in range(test_list):
#     if len(test_list[i])==0:
#         newList.apend(test_list[i])