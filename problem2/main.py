def caesar(offset,input_str):
    hasil=''
    for i in range (len(input_str)) :
        teks=input_str[i]
        if teks.isupper() :
            hasil += chr((ord(teks)+offset-65) % 26 +65)
        else :
            hasil+= chr((ord(teks)+offset-97)%26+97)
    return hasil

if __name__ == '__main__':
    print(caesar(3, "abc")) # def
    print(caesar(2, "alta")) # cnvc
    print(caesar(10, "alterraacademy")) # kvdobbkkmknowi
    print(caesar(1, "abcdefghijklmnopqrstuvwxyz")) # bcdefghijklmnopqrstuvwxyza
    print(caesar(1000, "abcdefghijklmnopqrstuvwxyz")) # mnopqrstuvwxyzabcdefghijkl