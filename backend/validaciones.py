#Funcion para las validaciones

from datos import clientes

def validar_campos(nombre, telefono, correo, ciudad):
    """Verificar que ninguno de los campos esten vacios"""

    if not nombre.strip():
        return False, "El nombre no puede quedar vacio"
    
    if not telefono.strip():
        return False, "El telefono no puede quedar vacio"
    
    if not correo.strip():
        return False, "El correo no puede quedar vacio"
    
    if not ciudad.strip():
        return False, "La ciudad no puede quedar vacia"
    
    return True, ""


def validar_nombre(nombre):
    "El nombre no puede contener numeros"

    if any(caracter.isdigit() for caracter in nombre):
        return False, "El nombre no puede contener numeros"
    
    return True, ""

def validar_ciudad(ciudad):
    "La cuidad no puede contener numeros"
    
    if any(caracter.isdigit() for caracter in ciudad):
        return False, "La ciudad no puede contener numeros"
    
    return True, ""

def validar_telefono(telefono):
    "El telefono solo debe que contener numeros"

    if not telefono.isdigit():
        return False, "El telefono solo debe de contener numeros"
    
    return True, ""

def validar_correo(correo):
    "Validifacion basica del correo"

    if "@" not in correo or "." not in correo:
        return False, "Correo electronico no valido"
    
    return True, ""
    
def validar_id(id_cliente):
    "El ID no se debe de repetir"

    for clientes in clientes:
        if clientes ["id"]== id_cliente:
            return False, "El ID ya existe"
        
        return True, ""
