lista = eval(cargadas.innerHTML)
try:
    punto = eval(sombra.value)
    lista.append(eval(sombra.value))
    assert type(punto) == tuple
    cargadas.innerHTML = str(lista)
    sombra.value = ''
    mensaje.innerHTML = ''
    box_mensaje.style.display = "none"
except Exception as e:
    js.alert("Sombra no válida: " + str(e))

if cargadas.innerHTML == '[]':
    box_cargadas.style.display = "none"
else:
    box_cargadas.style.display = "block"