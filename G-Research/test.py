query = "76 38 +"
print("Query", query)

query =query.split(" ")

if (query[2]) == "+":
    print(int(query[0]) + int(query[1]))
elif (query[2]) == "-":
    print( int(query[0]) - int(query[1]))
elif (query[2]) == "*":
    print( int(query[0]) * int(query[1]))
elif (query[2]) == "/":
    print( int(query[0]) / int(query[1]))

"""
if (query[1]) == "+":
    return int(query[0]) + int(query[2])
elif (query[1]) == "-":
    return int(query[0]) - int(query[2])
elif (query[1]) == "*":
    return int(query[0]) * int(query[2])
elif (query[1]) == "/":
    return int(query[0]) / int(query[2])
"""