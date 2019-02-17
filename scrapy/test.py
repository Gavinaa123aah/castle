# write to json
import json
# s=[{"name":"ljd","age":10},{"name":"zl","age":20}]
# with open("details.json","w")as f:
#     json.dump(s,f)



#read from json
# with open("details.json","r")as load_f:
#     dict_data = json.load(load_f)
#     print dict_data


# read urls from restaurants_details
# with open("restaurants_details",'r') as f:
#     while True:
#         line = f.readline()
#         if not line:
#             break
#         print line

with open("150_hotels_name.json", "r") as f_name:
    json_s = f_name.read()
print json_s

