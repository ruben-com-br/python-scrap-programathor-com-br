import json
import copy

def adicionar_arquivo_json(novo_dado, filename='vagas.json'):
    
    with open(filename,'r+') as arquivo:
        
        # Arquivo para objeto dict
        json_dict = json.load(arquivo)
        
        json_dict_antes = copy.deepcopy(json_dict)
        
        # Adiciona o novo dado
        json_dict['vagas'].update(novo_dado)
        
        # se true então tem uma vaga gravada no Json
        if ( json_dict_antes == json_dict ):
            print('vaga já presente no JSON')
            #return True se quiser parar
            return False
        else:
            print('vaga nova no JSON')
            # Define a posição atual do arquivo no deslocamento.
            arquivo.seek(0)

            # convert back to json.
            json.dump(json_dict, arquivo,  indent = 4)
            return False