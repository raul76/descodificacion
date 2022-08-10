lista = eval(cargadas.innerHTML)
abscisas = []
ordenadas = []
try:
    for punto in lista:
        assert type(punto) == tuple and len(punto) ==2
        abscisa, ordenada = punto
        abscisas.append(abscisa)
        ordenadas.append(ordenada)
    cifrado = termino(abscisas, ordenadas)
    descifrado = numero_a_texto(cifrado)
    mensaje.innerHTML = descifrado
    box_mensaje.style.display = "block"
except Exception as e:
    js.alert("Error al descifrar. Tal vez no son todas las sombras válidas o hay dos con la misma abscisa: " + str(e))
