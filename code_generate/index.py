import base64


def main():
    while True:
        print("ENCODE AND DECODE")
        print("*" * 31 + "MAIN MENU" + "*" * 32 + "\n"     
              "\t(E) ENCODE\n"                              
              "\t(D) DECODE\n" 
              "\t(R) RESET\n"    
              "\t(T) EXIT\n")
        input_1 = input("Please Select Your Operation: ")
        if (len(input_1) == 1):
            if(input_1 == 'E'):
                def_encode()
                break
            elif(input_1 == 'D'):
                def_decode()
                break
            elif(input_1 == 'R'):
                main()
                break
            elif(input_1 == 'T'):
                print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")
                break
            else:
                print("Error:Invalid!")
        else:
            print("Error!Invalid")    
#encode
def def_encode():
    while True:
        input_1 = input("Encode message: ")
        input_bytes = input_1.encode('ascii')       # input_1 string 'ascii'cannot convert into bytes
        base64_byte = base64.b64encode(input_bytes) #that's why base64.b64encode convert the input into encode-bynary number
        base64_string = base64_byte.decode('ascii') #original decode output
        print("Result: "+ base64_string)
        main()
       
#decode
def def_decode():
    while True:
        input_1 = input("Decode message: ")
        input_byte = input_1.encode('ascii')                 # input_1 bytes 'ascii'cannot convert into string
        base64_string_byte = base64.b64decode(input_byte)    #that's why base64.b64encode convert the input into decode-bynary number
        base64_string = base64_string_byte.decode('ascii')   #original decode string
        print("Result: " + base64_string)
        main()
       




if __name__ == "__main__":
    main()    