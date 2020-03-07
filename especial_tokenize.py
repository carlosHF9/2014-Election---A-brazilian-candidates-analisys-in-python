
from Lista import Lista

def remove_par(text):
    nova_palavra = ''
    for x in text:
        if x != '"':
            nova_palavra += x
    return nova_palavra

def special_tokenize(text):
    data_list = []
    new_text = ''
    for dados in text:
        if dados != ';':
            new_text += dados
        else:
            data_list.append(new_text)
            new_text = ''
    for i in range(len(data_list)):
        data_list[i] = remove_par(data_list[i])
        
    return data_list

def new_tokenize(text):
    data_list = Lista()
    new_text = ''
    for dados in text:
        if dados != ';':
            new_text += dados
        else:
            data_list.anexar(new_text)
            new_text = ''
    for i in range(data_list.size):
        data_list[i] = remove_par(data_list[i])
        
    return data_list




    
