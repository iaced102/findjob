def demo_split(string, parameter1) :
    result = []
    word = ""
    for i in range(len(string)) :
        if parameter1 == "" :
            result.append(string[i])
        elif parameter1 == "''" :
            result.append(string[i])
        else:
            if string[i] != parameter1 :
                word += string[i]
            else:
                result.append(word)
                word=''
    return result
print(demo_split('xin chao cac ban ', " "))