#Libraries
import re
import utils


#function to return each letter index
def find_pos(character,cadena_alf):
    posi=0
    for i in range(len(cadena_alf)):
        if character==cadena_alf[i]:
            posi=i
            return posi
        

#function to return each lowercase letter index

def find_posLow(character,cadena_alf):
    posi=0
    for i in range(len(cadena_alf.lower())):
        if character==cadena_alf[i].lower():
            posi=i
            return posi
        

# cipher for each character
def cipher(letter,key,cadena_alf):
    codi=""
    if letter.isupper():
        psc=find_pos(letter,cadena_alf)
        if psc>=0:
            pos2=(psc+key)% len(cadena_alf)
            codi=cadena_alf[pos2]
           
     
    elif letter.islower():
        psc=find_posLow(letter,cadena_alf)
        if psc>=0:
            pos2=(psc+key)% len(cadena_alf.lower())
            codi=cadena_alf[pos2].lower()
            
           
    elif letter.isdigit:
        codi=str(letter)
       

    elif re.fullmatch(r'[:punt:]',letter):
        codi=str(letter)
        

    else:
        codi=" "
            

    return codi


#Phrase Encryptor


def encryptor_C(phrase,despl,cadena_alf):
    msj_encript=""

    for element in phrase:
        print(cipher(element,despl,cadena_alf))
        msj_encript+=cipher(element,despl,cadena_alf)
        
    
    print(msj_encript)


def main():
    check=True
    opc=1
    def executer():
            utils.art_decor()
            phrase=input("\nIngresa la cadena a cifrar: ")
            try:
                despl=int(input("Ingresa el numero de desplazamiento:\n "))
                selec=int(input("Ingresa la opcion de alfabeto 1 Espanol 2 Ingles: "))
                while (selec!=1) and (selec!=2):
                    print("Opcion invalida intente de nuevo con un valor valido")
                    break

                else:
                     cadena_alf=utils.list_Alf(selec)
                     encryptor_C(phrase,despl,cadena_alf)
                
                    
                    
                   
            except ValueError:
                print("Opcion invalida intente de nuevo con un valor valido")
                
            
    while check:
        while opc==1:
            executer()
            try:
                opc=int(input("Ingresa 1 para volver a cifrar otra frase, y  cualquier otro numero para salir. "))
            except ValueError:
                 print("Opcion invalida intente de nuevo con un valor valido")
                
            
        else:
            check=False
            print("__FIN__")
            break
                           
     
                  
            
    
                  
        

if __name__ =='__main__':
    main()
    
