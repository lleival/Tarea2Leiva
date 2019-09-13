def tarea2 (A,B):

    respuesta=[]

    if type(A)==int and type(B)==int:

        if  A >= B:

            respuesta = [A-B,A+B,A*B]

            return respuesta

        else:
            return -1

    else:
        return -1
