def check(num):
    if num in range(-5, 5):
        return True
    else:
        return False

print(check(-6))
print(check(5))
print(check(4))

print("--------------------------------------------------------------")


def make_dict(list1, list2):
    return {list1[i]: list2[i] for i in range(len(list1))}


print(make_dict(["a", "b"], [1, 2]))

print("--------------------------------------------------------------")


def squares_list():
    return [i**2 for i in range(1, 31)]


print(squares_list())
print("--------------------------------------------------------------")


def modify_list():
    list = [3, 6, 4, 0, 8]
    print(f"original ist {list}")

    list.pop()
    print(f"after remove the last element {list}")

    list.insert(1, "R")
    print(f"after insert R at 1st position {list}")

    number = int(input("Enter a number to delete from list: "))
    if number in list :
        list.remove(number)
        print(f"after remove {number} from list {list}")
    else:
        print(f"{number} not in list")

modify_list()

print("--------------------------------------------------------------")

def compine_dict(dict1,dict2):
    new_dict = dict1.copy()
    for key, value in dict2.items():
        if key not in new_dict:
            new_dict[key] = value
    return new_dict
    # return {**dict1,**dict2}

print(compine_dict({"a":1,"b":2},{"b":2,"c":3,"d":4}))   
print(compine_dict({"a":1,"b":2},{"c":3,"d":4,"e":5}))    
