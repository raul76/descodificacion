import js

box_cargadas = js.document.getElementById("box-cargadas")
box_mensaje = js.document.getElementById("box-mensaje")
sombra = js.document.getElementById("txtSombra")
cargadas = js.document.getElementById("cargadas")
mensaje = js.document.getElementById("mensaje")

#### Aquí ponemos las funciones de Python necearias para este proyecto

def numero_a_texto(num):
  """
    Metemos un número y lo transforma en texto, dividiéndolo de 3 en 3 y tomando 
    cada bloque como un código unicode. Se completa con ceros a la izquierda si
    no hay un número de digitos que sea múltiplo de tres.
  """
  cadena = str(num)
  if len(cadena) % 3:   # Entra cuando no hay un múltiplo de tres dígitos
    cadena = (3- len(cadena) % 3) * '0' + cadena
  caracteres = []
  for idx in range(0, len(cadena), 3):
    trozo = cadena[idx:idx+3]
    num = int(trozo)
    caracteres.append(chr(num))
  return ''.join(caracteres)


def vandermonde(lista):
  """
      Resuelve un determinante de Vandermonde.
  """
  if len(lista) == 1:
    return 1
  siguiente = lista.copy()
  ultimo = siguiente.pop()
  resultado = 1
  for valor in siguiente:
    resultado *= (ultimo - valor)
  return resultado * vandermonde(siguiente)


def vandermonde_mod(lista, columna):
  """
     Resuelve un determinante de Vandermonde modificado,
     útil para calcular el término independiente del polinomio
     interpolador.
  """
  resultado = 0
  signo = 1
  for idx in range(len(columna)):
    lista_aux = lista.copy()
    elemento = lista_aux.pop(idx)
    prefijo = 1
    for valor in lista_aux:
      prefijo *= valor
    parcial = columna[idx] * signo * prefijo * vandermonde(lista_aux)
    resultado += parcial
    signo *= -1
  return resultado 

def termino(lista, columna):
  """
  Introducida la lista con las abscisas de las sombras y la columna con las ordenadas
  de dichas sombras, se devuelve el número que debería tener el mensaje en código unicode.
  """
  return vandermonde_mod(lista, columna) // vandermonde(lista)  # División entera, no queremos que aproxime un float.