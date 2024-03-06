def compare(a, b):
    if len(a) > len(b) :
        start_index = a.index(b)
        end_index= len(b)
        pattern =a[start_index:end_index]
    else :
        start_index =b.index(a)
        end_index=len(a)
        pattern =b[start_index:end_index]

    return pattern

if __name__ == '__main__':
    print(compare("AKA", "AKASHI")) # AKA
    print(compare("KANGOORO", "KANG")) # KANG
    print(compare("KI", "KIJANG")) # KI
    print(compare("KUPU-KUPU", "KUPU")) # KUPU
    print(compare("ILALANG", "ILA")) # ILA