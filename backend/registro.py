from datos import clientes
from validaciones import *

def registrar_cliente(id_cliente, nombre, telefono, correo, ciudad):

    valido, mensaje = validar_id(id_cliente)
    if not valido:
        return False, mensaje
    
    valido, mensaje = validar_campos(nombre, telefono, correo, ciudad)
    if not validar_correo:
        return False, mensaje
    
    valido, mensaje = validar_nombre(nombre)
    if not validar_nombre:
        return False, mensaje
    
    valido, mensaje = validar_ciudad(ciudad)
    if not validar_ciudad:
        return False, mensaje
    
    valido, mensaje = validar_telefono(telefono)
    if not validar_telefono:
        return False, mensaje
    
    valido, mensaje = validar_correo(correo)
    if not validar_correo:
        return False, mensaje
    
    clientes = {

        "id": id_cliente,

        "nombre": nombre,

        "telefono": telefono,

        "correo": correo,

        "ciudad": ciudad
    }

    clientes.append(clientes)

    return True, "El cliente ha sido registrado de manera exisitosa"
