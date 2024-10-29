def func_index_listas(x):
    mi_lista = [10,20,30,40,50,60,70,80,90,100]
    
    if x not in mi_lista:
        print("Número no presente en la lista")
    else:
        mi_index = mi_lista.index(x)
        
        print(f'El indice del número elegido es: {mi_index}')