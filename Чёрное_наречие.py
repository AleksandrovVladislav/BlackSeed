def Black_Speech(code):
    python_commands = ['input','print','int', 'str', 'float', 'len', 'replace', 'split', 'lower', 'upper', 'append', 'remove', 'if', 'elif', 'else', 'not', 'for', 'in', 'range', 'break', 'continue', 'while', 'def', 'True', 'False', 'impoort', 'random', 'randint']
    for i in python_commands:
        if i in code:
            print('Prakhurz hu-na')
            return  ''
    code = code.replace('ert', '')
    code = code.replace('hu-na', 'input')
    code = code.replace('margim', 'print')
    code = code.replace('gunod', 'int')
    code = code.replace('hul', 'str')
    code = code.replace('krur', 'float')
    code = code.replace('sigum', 'len')
    code = code.replace('bhad', 'replace')
    code = code.replace('sorgh', 'split')
    code = code.replace('gukh', 'lower')
    code = code.replace('talug', 'upper')
    code = code.replace('marbh', 'append')
    code = code.replace('khara', 'remove')
    code = code.replace('ak', 'if')
    code = code.replace('rag', 'elif')
    code = code.replace('nanulg', 'else')
    code = code.replace('arg', 'not')
    code = code.replace('ar', 'for')
    code = code.replace('dau', 'in')
    code = code.replace('dunudum', 'range')
    code = code.replace('atishum', 'break')
    code = code.replace('fal', 'while')
    code = code.replace('buf', 'def')
    code = code.replace('kogurz', 'True')
    code = code.replace('furuzm', 'False')
    code = code.replace('horm', 'import')
    code = code.replace('fasharz', 'random')
    code = code.replace('asharz', 'randint')
    exec(code)
