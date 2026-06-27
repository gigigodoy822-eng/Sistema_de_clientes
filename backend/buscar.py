#Buscar un cliente por medio de su ID

from datos import clientes

def buscar_cliente(id_cliente):
    "Buscar un cliente por medio de su ID "
    
    "parametro:"
    "id_cliente(int)"
    
    "Retorna:"
    "dict -> si lo encuentra" 
    "None -> si no existe"

    for clientes in clientes:

        if clientes["id"] == id_cliente:
            return clientes
        
    return None
