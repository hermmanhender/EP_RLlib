
def persianas_OnOff(Ti, SP_temp, dT_up, dT_dn, Bw, action_p):
    '''
    # Persianas On-Off
    Esta función permite la operación binaria (completamente cerrada [On] o completamente abierta [Off]) de una persiana a partir de reglas fijas.

    * Ti es la temperatura interior
    * SP_temp es el valor de temperatura de confort
    * dT_up es el límite superior para el rango de confort
    * dT_dn es el límite inferior para el rango de confort
    * Bw es la radiación solar directa que existe en el plano de la ventana
    '''
    """Control de la persiana"""
    if Ti >= (SP_temp + dT_up) and Bw == 0:
        action_p = 0 #Abrir la persiana
    elif Ti >= (SP_temp + dT_up) and Bw > 0:
        action_p = 1 #Cerrar la persiana
        
    elif Ti <= (SP_temp - dT_dn) and Bw == 0:
        action_p = 1
    elif Ti <= (SP_temp - dT_dn) and Bw > 0:
        action_p = 0
        
    elif Ti < (SP_temp + dT_up) and Ti > (SP_temp - dT_dn):
        action_p = action_p

    else:
        print("Control de la persiana fallido")
        action_p = -1
    
    return action_p

###########################################################################################################################

def acondicionador_OnOff(Ti, SP_temp, dT_up, dT_dn, action_aa):
    '''
    # Aire Acondicionado On-Off
    Esta función permite la operación binaria (encendido [On] o apagado [Off]) de un equipo de aire acondicionado a partir de reglas fijas.

    * Ti es la temperatura interior
    * SP_temp es el valor de temperatura de confort
    * dT_up es el límite superior para el rango de confort
    * dT_dn es el límite inferior para el rango de confort
    '''
    
    if Ti >= (SP_temp + dT_up):
        action_aa = 1

    elif Ti <= (SP_temp - dT_dn):
        action_aa = 0

    elif Ti < (SP_temp + dT_up) and Ti > (SP_temp - dT_dn):
        action_aa = action_aa

    else:
        print("Control de Aire Acondicionado Fallido")
        action_aa = -1
    
    return action_aa

###########################################################################################################################

def coolandheat_OnOff(Ti, SP_temp, dT_up, dT_dn, action_aa, action_c):
    '''
    # Aire Acondicionado On-Off
    Esta función permite la operación binaria (encendido [On] o apagado [Off]) de un equipo de aire acondicionado a partir de reglas fijas.

    * Ti es la temperatura interior
    * SP_temp es el valor de temperatura de confort
    * dT_up es el límite superior para el rango de confort
    * dT_dn es el límite inferior para el rango de confort
    '''
    
    if Ti >= (SP_temp + dT_up):
        action_aa = 1
        action_c = 0

    elif Ti <= (SP_temp - dT_dn):
        action_aa = 0
        action_c = 1

    elif Ti < (SP_temp + dT_up) and Ti > (SP_temp - dT_dn):
        action_aa = action_aa
        action_c = action_c

    else:
        print("Control de Aire Acondicionado Fallido")
        action_aa = -1
        action_c = -1
    
    return action_aa, action_c

###########################################################################################################################

def calefactor_OnOff(Ti, SP_temp, dT_up, dT_dn, action_aa):
    '''
    # Calefactor On-Off
    Esta función permite la operación binaria (encendido [On] o apagado [Off]) de un equipo de aire acondicionado a partir de reglas fijas.

    * Ti es la temperatura interior
    * SP_temp es el valor de temperatura de confort
    * dT_up es el límite superior para el rango de confort
    * dT_dn es el límite inferior para el rango de confort
    '''
    
    if Ti >= (SP_temp + dT_up):
        action_aa = 0

    elif Ti <= (SP_temp - dT_dn):
        action_aa = 1

    elif Ti < (SP_temp + dT_up) and Ti > (SP_temp - dT_dn):
        action_aa = action_aa

    else:
        print("Control de Calefactor Fallido")
        action_aa = -1
    
    return action_aa

###########################################################################################################################

def ventana_OnOff(Ti, To, SP_temp, dT_up, dT_dn, action_v):
    '''
    # Ventana On-Off
    Esta función permite la operación binaria (encendido [On] o apagado [Off]) de una ventana a partir de reglas fijas.
    '''
    
    if Ti >= (SP_temp + dT_up):
        if Ti > To:
            action_v = 1
        else:
            action_v = 0

    elif Ti <= (SP_temp - dT_dn):
        if Ti > To:
            action_v = 0
        else:
            action_v = 1

    elif Ti < (SP_temp + dT_up) and Ti > (SP_temp - dT_dn):
        action_v = action_v

    else:
        print("Control de Ventana Fallido")
        action_v = -1
    
    return action_v

###########################################################################################################################

def ventana_OnOff2(Ti, To, SP_temp, dT_up, dT_dn, RHi, RH_SP, action_v):
    '''
    # Ventana On-Off
    Esta función permite la operación binaria (encendido [On] o apagado [Off]) de una ventana a partir de reglas fijas.
    '''
    
    if Ti >= (SP_temp + dT_up) or RHi > RH_SP:
        if Ti > To or RHi > RH_SP:
            action_v = 1 #abrir
        else:
            action_v = 0 #cerrar

    elif Ti <= (SP_temp - dT_dn):
        if Ti > To:
            action_v = 0
        else:
            action_v = 1

    elif Ti < (SP_temp + dT_up) and Ti > (SP_temp - dT_dn):
        action_v = action_v

    else:
        print("Control de Ventana Fallido")
        action_v = -1
    
    return action_v

###########################################################################################################################

def temperature_schedule(hora):

    if hora <= 7 or hora >= 23:
        Theat = 17
        Tchill = 28
    
    elif hora > 7 and hora < 23:
        Theat = 20
        Tchill = 25

    return Theat, Tchill