from SeccionPractica import tarea2


def test_casoExito():
    assert tarea2(5, 1) == [4, 6, 5]


def test_casoError1():
    assert tarea2(5, 8) == -1


def test_casoError2():
    assert tarea2("a", 8) == -1
