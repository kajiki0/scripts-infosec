'''
Uso: python num_to_md5.py <numero_inicial> <numero_final>

sera gerado ao final do script um arquivo hashes_md5.txt para facilitar o uso ao aplicar wordlists
para brute force (ex: IDs de usuarios)

'''


import hashlib
import sys


if len(sys.argv)<3:
    print("ERRO! faltam argumentos")
    sys.exit(1)



def gen_md5(num_i,num_f):
    lista_numeros_md5 = []
    
    for num in range(num_i,num_f+1):
        #numero para string para byte
        string_bytes = str(num).encode('utf-8')    
        
        #gerar md5 e retornar em hexadecimmal
        numero_convertido_md5 = hashlib.md5(string_bytes).hexdigest()
        lista_numeros_md5.append(numero_convertido_md5)


    return lista_numeros_md5
        



num_inicial = int(sys.argv[1])
num_final = int(sys.argv[2])

lista_hash = gen_md5(num_inicial,num_final)

# facilitar quando for usar para brute force
with open("hashes_md5.txt","w") as arquivo:
    arquivo.write("\n".join(lista_hash))
