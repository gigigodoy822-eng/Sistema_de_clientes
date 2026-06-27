#Se busca eliminar a un cliente

from datos import clientes
from buscar import buscar_cliente

def eliminar_cliente(id_cliente):
    "Se elimina un cliente mediante su ID"

    clientes = buscar_cliente(id_cliente)

    if clientes is None:
        return False, "Cliente no encontrado"
    
    clientes.remove(clientes)
    return True, "Cliente eliminado de manera correcta"
