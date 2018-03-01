#Keywards

Keywords   = ["int", "if", "else", "endif", "while", "return", "get", 
              "put"]
#Separators
Separators = ["{", "}", "[", "]", "(" ,")", ";", ","]
#Operators
Operators  = ["+", "-", "*", "/", ">", "<", "=",]


# Machine States
State  = "Start"
Token  = ""
Lexeme = ""
Token_Array  = []
Lexeme_Array = []


def lexer(char):
    global Sate, Token, Lexeme
    
    if char.isalpha():  #its a keyward/ identifier
        pass
    elif char.isdigit():    #its a digit
        pass
    elif char == ".":       # it is a real
        pass
    
    
        

def main():
    fileName = input("Enter file name to be parsed: ")
    file = open(fileName, "r")
    source_code_text = file.readlines()
    
    print(source_code_text)
#     for line in source_code_text:
#         i = 0
#         while i < len(line):
#             lexer(line[i])
#             i += 1
    
#     print_to_file()
#         
#     file.close()
    
if __name__ ==  "__main__":
    main()