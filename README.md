# CPSC323

#  Assignment 1 - Lexical Analysis

Project Team: 		1. Aishwarya Iyer (https://github.com/aishiyer)
					2. Abhishek Mhatre (https://github.com/aB9s) 
					
				
The programming assignments are based on a language called "Rat18S" which is described as
follows. The Rat18S language is designed to be an easy to understand.  It has a short grammar and  relatively clean semantics.  

1) Lexical Conventions:
>>The lexical units of a program are identifiers, keywords, integers, reals, operators and other 
separators.  
>>Blanks, tabs and newlines (collectively, "white space") as described below are ignored except as they serve to separate tokens.
>>Some white space is required to separate otherwise adjacent identifiers, keywords, reals and integers.
>><Identifier> is a sequence of letters or digits, however, the first character must be a letter and last char must be either $ or letter. Upper and lower cases are same.
>><Integer>  is an unsigned decimal integer i.e., a sequence of decimal digits.
>><Real> is integer followed by “.” and Integer, e.g., 123.00
>>Some identifiers are reserved for use as keywords, and may not be used otherwise:
       e.g.,  int, if, else, endif,  while, return, get, put   etc.
>>Comments are enclosed in    !         !