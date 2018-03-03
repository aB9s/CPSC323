#Keywards
Keywords   = ["int", "float", "boolean" ,"if", "else", "endif", "while", "return", "get", "put","function","for"]
#Separators
Separators = ["{", "}", "[", "]", "(" ,")", ";", ",",":"]
#Operators
Operators  = ["+", "-", "*", "/", ">", "<", "=","!","&" ]
#Double Operators
Double_Operators = ["+=","-=","*=","/=","%=","==","<=",">=","!="]
 
 
# Machine States
buffer_token = ""
Token_Array  = []
Lexeme_Array = []
Buffer_Array =[]
 
def crateBuffer(char):
    global buffer_token
    if char.isalpha() or char.isdigit(): #possible identifier, keyword, integer or real
        if buffer_token !="" and buffer_token[-1] in Operators:
            Buffer_Array.append(buffer_token)
            buffer_token = ""
        buffer_token +=char
    elif char =="$":                     #possible identifier (last letter of the identifier should be a letter or a $ sign 
        buffer_token+=char
    elif buffer_token.isdigit() and char ==".":      #all characters in the buffer are digit and '.' (dot) appeared--> possible real 
        buffer_token+=char
    elif char in Separators:            #Separator
        Buffer_Array.append(buffer_token)
        Buffer_Array.append(char)
        buffer_token = ""
    elif char in Operators:             #Operator        
        if buffer_token =="":
            buffer_token+=char
#             Buffer_Array.append(buffer_token)
        elif buffer_token != "" and buffer_token[-1] in Operators:     #already an operator present in the buffer --> could be a double operator
            buffer_token+=char
        elif buffer_token[-1].isalpha() or buffer_token[-1].isdigit():
            Buffer_Array.append(buffer_token)
            buffer_token = char
        else:
            buffer_token+=char
            Buffer_Array.append(buffer_token)
            buffer_token = ""
    elif char==" " or char=="\n" or char =="\t":        # Unknown
        if char =="!":
            buffer_token+= char
        Buffer_Array.append(buffer_token)
        buffer_token =""
    
    
def lexer(Buffer_Array):
    token = ""
    lexeme = ""
    
    for char in Buffer_Array:
       #If its an empty space, just ignore it
        if len(char) > 0:
            #Process
            for c in char:
                #Beginning of comment section
                if c =="!" and (token =="Unknown" or token ==""):
                    token = "Comment"
                    #End of the comment section
                elif c =="!" and token =="Comment":
                    token =""
                elif c.isalpha():
                    #Its a part of comment section, ignore it
                    if token =="Comment":
                        pass
                    elif token=="" or token=="Identifier":
                        lexeme +=c
                        token = "Identifier"
                        #Identifier
                elif c =="$" and token =="Identifier":
                    lexeme +=c
                    token = "Identifier"
                elif c.isdigit():
                    if token =="" or token =="Integer":
                        lexeme+=c
                        token = "Integer"
                    elif token =="Real":
                        lexeme +=c
                        token = "Real"
                    else:
                        lexeme +=c
                        token = "Unknown"
                elif c ==".":
                    #Its a object and function separator or an unknown
                    if token == "Identifier" or token =="Unknown":
                        Token_Array.append(token)
                        Lexeme_Array.append(lexeme)
                        token = ""
                        lexeme= ""
                    #its a real value
                    elif token == "Integer":                                
                        lexeme +=c
                        token = "Real"
                    else:
                        Token_Array.append(token)
                        Lexeme_Array.append(lexeme)
                        token = ""
                        lexeme= ""
                elif c in Separators:
                    token = "Separator"
                    Token_Array.append(token)
                    token = ""
                    lexeme += c
                    Lexeme_Array.append(lexeme)
                    lexeme = ""
                elif c in Operators:
                    if token=="":
                        token = "Operator"
                        lexeme += c
                    else:
                        token = "Operator"
                        Token_Array.append(token)
                        token = ""
                        lexeme += c
                        Lexeme_Array.append(lexeme)
                        lexeme = ""
            if token =="Identifier" and lexeme in Keywords:
                token = "Keyword"
                Token_Array.append(token)
                token = ""
                Lexeme_Array.append(lexeme)
                lexeme = ""
            elif token =="Identifier" or token=="Integer" or token=="Real" or token =="Separator" or token =="Operator" or token =="Unknown":
                Token_Array.append(token)
                token = ""
                Lexeme_Array.append(lexeme)
                lexeme= ""
            
            elif token =="Comment":
                pass  
        else:
            if token =="Identifier" and lexeme in Keywords:
                Token_Array.append(token)
                token = ""
                Lexeme_Array.append(lexeme)
                lexeme = ""
            elif token =="Identifier" or token =="Unknown":
                Token_Array.append(token)
                token = ""
                Lexeme_Array.append(lexeme)
                lexeme= ""
            elif token =="Comment":
                pass
            else:
                Token_Array.append(token)
                token = ""
                Lexeme_Array.append(lexeme)
                lexeme = ""
     
     
             
            
    #### EDIT THIS FUNCTION ####    
def print_to_file():
    outputFile = open("lexer_output" + ".txt", "w")
    outputFile.write("Token" + "\t\t\t" + "Lexeme\n")
    outputFile.write("-------------------------------\n")
    i = 0
    while i < len(Token_Array):
        if Token_Array[i] != "":
            if Token_Array[i] == "Keyword" or Token_Array == "Unknown" or Token_Array[i] == "Integer" or Token_Array[i] == "Real":
                outputFile.write(Token_Array[i] + "\t\t\t" + Lexeme_Array[i] + "\n")
                
            else:
                outputFile.write(Token_Array[i] + "\t\t" + Lexeme_Array[i] + "\n")
        i += 1
    outputFile.close()    
         
 ##Main method
def main():
    fileName = input("Enter name of source file to be parsed: ")
    file = open(fileName, "r")
    source_code_text = file.readlines()
     
    for line in source_code_text:
        i = 0
        while i < len(line):
            crateBuffer(line[i])
            i += 1
            
    lexer(Buffer_Array)
    print(Buffer_Array)
     
    print_to_file()
 
    file.close()
     
if __name__ ==  "__main__":
    main()