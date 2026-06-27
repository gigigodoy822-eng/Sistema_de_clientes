#Editar a un cliente

from buscar import buscar_cliente
from validaciones import (
    validar_campos,
    validar_nombre,
    validar_ciudad,
    validar_telefono,
    validar_correo,
)

def editar_cliente(id_cliente, nombre, telefono, correo, ciudad):

    clientes = buscar_cliente(id_cliente)

    if clientes is None:
        return False, "El cliente no ha sido encontrado"
    
    for funcion in (
        lambda: validar_campos(nombre, telefono,correo, ciudad),
        lambda: validar_nombre(nombre),
        lambda: validar_ciudad(ciudad),
        lambda: validar_telefono(telefono),
        lambda: validar_correo(correo),
    ):
        valido, mensaje = funcion()
        if not valido:
            return False, mensaje
        
    clientes["nombre"]= nombre
    clientes["telefono"]= telefono
    clientes["ciudad"]= ciudad
    clientes["correo"]= correo

    return True, "El cliente ha sido actualizado de manera correcta"
