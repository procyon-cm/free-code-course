def arithmetic_arranger(problems, *args):
    EMPTY_SPACE = ' '

    lst_1_line = list()                                                 # final lists
    lst_2_line = list()
    lst_dashes = list()
    lst_result = list()
    
    for problem in problems:
        num_and_oper = problem.split()                                  # splitting each problem to numbers and operators
        num_1 = num_and_oper[0]
        num_2 = num_and_oper[2]
        operator = num_and_oper[1]
        
        # exceptions leading to error
        try:                                                            # number should only contain digits
            num_1_int = int(num_1)
            num_2_int = int(num_2)
        except:
            return 'Error: Numbers must only contain digits.'
        if len(problems) > 5:
            return 'Error: Too many problems.'
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        if len(num_1) > 4 or len(num_2) > 4:                            
            return 'Error: Numbers cannot be more than four digits.'

        
        # count of spaces before numbers
        longer_num = max([num_1, num_2], key=len)           # finds the longest num (1 or 2)
        total_length = len(longer_num) + 2                  # total lenght of the problem (num + one space + operator)
        
        first_line = EMPTY_SPACE * (total_length - len(num_1)) + num_1
        lst_1_line.append(first_line)
        
        second_line = operator + EMPTY_SPACE * (total_length - len(num_2) - 1) + num_2
        lst_2_line.append(second_line)

        line_of_dashes = '-' * (total_length)
        lst_dashes.append(line_of_dashes)
        
        if operator == '+':                                 # counting the result
            result = num_1_int + num_2_int
        else:
            result = num_1_int - num_2_int

        line_of_results = EMPTY_SPACE * (total_length - len(str(result))) + str(result)
        lst_result.append(line_of_results)

    def construct_line(input: list):
        return '    '.join(input)    
        
    line_1 = construct_line(lst_1_line)
    line_2 = construct_line(lst_2_line)    
    line_3 = construct_line(lst_dashes)    
    line_4 = construct_line(lst_result)

    arranged_problems = line_1 + '\n' + line_2 + '\n' + line_3
    if args:
        arranged_problems += '\n' + line_4

    return arranged_problems
           