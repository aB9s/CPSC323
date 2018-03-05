#Keywords
Keywords   = ["int", "float", "boolean" ,"if", "else", "endif", "while", "return", "get", "put","function","for"]
#Separators
Separators = ["{", "}", "[", "]", "(" ,")", ";", ",",":"]
#Operators
Operators  = ["+", "-", "*", "/", ">", "<", "=","!","&" ]
#Double Operators
Double_Operators = ["+=","-=","*=","/=","%=","==","<=",">=","!="]
 
# File name without extension
source_filename = ""
# Machine States
buffer_token = ""
Token_Array  = []
Lexeme_Array = []
Buffer_Array =[]
 
def crateBuffer(char):
    global buffer_token
    #identifier/ keyword/ integer/ real
    if char.isalpha() or char.isdigit():
        if buffer_token !="" and buffer_token[-1] in Operators:
            Buffer_Array.append(buffer_token)
            buffer_token = ""
        buffer_token +=char
    #identifier (last letter of the identifier should be a letter or a $ sign)
    elif char =="$":                      
        buffer_token+=char
    #all characters in the buffer are digit and '.' (dot) appeared--> possible real
    elif buffer_token.isdigit() and char ==".":       
        buffer_token+=char
    #Separator
    elif char in Separators:            
        Buffer_Array.append(buffer_token)
        Buffer_Array.append(char)
        buffer_token = ""
    #Operator
    elif char in Operators:                     
        if buffer_token =="":
            buffer_token+=char
#             Buffer_Array.append(buffer_token)
        #already an operator present in the buffer --> could be a double operator
        elif buffer_token != "" and buffer_token[-1] in Operators:     
            buffer_token+=char
        elif buffer_token[-1].isalpha() or buffer_token[-1].isdigit():
            Buffer_Array.append(buffer_token)
            buffer_token = char
        else:
            buffer_token+=char
            Buffer_Array.append(buffer_token)
            buffer_token = ""
    # Unknown
    elif char==" " or char=="\n" or char =="\t":        
        if char =="!":
            buffer_token+= char
        Buffer_Array.append(buffer_token)
        buffer_token =""
    
    ###Function to # 
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
                #Identifier/ Keyword
                elif c.isalpha():
                    #Its a part of comment section, ignore it
                    if token =="Comment":
                        break
                    elif token=="" or token=="Identifier":
                        lexeme +=c
                        token = "Identifier"
                #Identifier
                elif c =="$" and token =="Identifier":
                     #Its a part of comment section, ignore it
                    if token =="Comment":
                        break
                    else:
                        lexeme +=c
                        token = "Identifier"
                #Integer/ Real
                elif c.isdigit():
                     #Its a part of comment section, ignore it
                    if token =="Comment":
                        break
                    elif token =="" or token =="Integer":
                        lexeme+=c
                        token = "Integer"                        
                    elif token =="Real":
                        lexeme +=c
                        token = "Real"
                    else:
                        lexeme +=c
                        token = "Unknown"
                # Real
                elif c ==".":
                     #Its a part of comment section, ignore it
                    if token =="Comment":
                        break
                    #Its a separator or an unknown
                    elif token == "Identifier" or token =="Unknown":
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
                     #Its a part of comment section, ignore it
                    if token =="Comment":
                        break
                    else:
                        token = "Separator"
                        Token_Array.append(token)
                        token = ""
                        lexeme += c
                        Lexeme_Array.append(lexeme)
                        lexeme = ""
                elif c in Operators:
                     #Its a part of comment section, ignore it
                    if token =="Comment":
                        break
                    elif token=="":
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
                
    #Clear the buffer for the next line
    Buffer_Array.clear()
    
    #### End of lexer() ####
     
             
            
    #### Function to print Tokens and Lexemes table into a file ####    
def print_to_file():
    outputFile = open(source_filename+"_lexer_output" + ".txt", "w")
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
    
    
    #### End of print_to_file() ####
         
def main():
    global source_filename
    #Get file 
    filename = input("Enter name of source file to be parsed: ")
    file = open(filename, "r")
    #Remove extension from the source filename
    source_filename = filename.split(".")[0]
    
    source_code_text = file.readlines()
     
    for line in source_code_text:
        i = 0
        
        while i < len(line):
            #Read each token from the source code line and add it into a buffer
            crateBuffer(line[i])
            i += 1
            
        #Sort tokens into lexemes
        lexer(Buffer_Array)
    
    
    #Print table to a file 
    print_to_file()
 
    #Close the file
    file.close()
    
    #### End of main() ####
     
if __name__ ==  "__main__":
    main()