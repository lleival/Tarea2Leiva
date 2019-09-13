from SeccionPractica import tarea2

def casoExito ():
    assert tarea2(5,1) == [4,6,5]
    
def casoError1 ():
    assert tarea2(5,8) == -1

def casoError2 ():
    assert tarea2("a",8) == -1
