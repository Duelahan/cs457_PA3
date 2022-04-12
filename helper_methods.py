#Author: Tristan Bailey
#Date Created: 3/15/2022
#Last Modified: 4/12/2022
#Assignment: PA 3
#Class: CS457
#File: File for the table methods

#helper function: returns the index of the keyword in the list of tokens, or -1 if keyword is not present in tokens
def keyword_index(tokens, keyword):
    exit = False
    index = 0
    while(not(exit) and (index < len(tokens))):
        if (tokens[index].lower() == keyword.lower()):
            exit = True
        else:
            index += 1
    if(index >= len(tokens)):
        return -1
    else:
        return index

#helper fuinction that converts tokens(strings) into thier appropriate datatypes
def convert_token(data_type, token):
    #int conversion
    if(data_type == "int"):
        return int(token)
    #float conversion
    elif(data_type == "float"):
        return float(token)
    #char conversion
    elif(data_type == "char"):
        return str(token)[0]
    #varchar conversion
    else:
        try:
            #remove ')' and then split string based on presence of '('
            temp_list = ((data_type)[:-1]).split("(")
            #check if cur string is larger than the max size allower for varchar
            #if it is make the appropriate reduction
            #if not then do nothing to it
            if(int(temp_list[1]) < len(token)):
                return token[:int(temp_list[1])]
            else:
                return token
        except:
            raise Exception("Invalid datatype for conversion")

def three_arg_lists(tokens, table_1_var, table_2_var):
    table_1_args = []
    table_2_args = []
    join_on_args = []
    #itterate through arguemnts by threes
    for arg in range(0, len(tokens), 3):
        left = tokens[arg]
        operator = tokens[arg + 1]
        right = tokens[arg + 2]
        #single table
        if(left[0].lower() == right[0].lower()):
            if(left[0].lower() == table_1_var.lower()):
                table_1_args.append(left[2:])
                table_1_args.append(operator)
                table_1_args.append(right[2:])
            elif(left[0].lower() == table_2_var.lower()):
                table_2_args.append(left[2:])
                table_2_args.append(operator)
                table_2_args.append(right[2:])
            else:
                #invalid operation
                pass
        #join on
        else:
            join_on_args.append(left)
            #$$$
            join_on_args.append("=")
            join_on_args.append(right)
    return table_1_args, table_2_args, join_on_args