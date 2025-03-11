while True:
    # Ciclo for para una mejor presentación
    for i in range(0, 25):
        print("")

    # Menu dónde se va a entrar a cada una de las herramientas o cerrar el programa
    menuprincipal = input("--------------------FCC ToolKit--------------------\n"
                          "Selecciona la herramienta a la que quieras acceder: \n"
                          "1 -> Tablas de Verdad\n"
                          "2 -> Teoría de Conjuntos\n"
                          "3 -> Calculadora de sucesiones\n"
                          "4 -> Relaciones y funciones\n"
                          "0 -> Salir del programa\n"
                          "Escogiendo la herramienta: ")
    while menuprincipal not in "01234":
        print("\n--Herramienta no encontrada. Vuelve a intentarlo.--\n\n")
        menuprincipal = input("--------------------FCC ToolKit--------------------\n"
                              "Selecciona la herramienta a la que quieras acceder: \n"
                              "1 -> Tablas de Verdad\n"
                              "2 -> Teoría de Conjuntos\n"
                              "3 -> Calculadora de sucesiones\n"
                              "4 -> Relaciones y funciones\n"
                              "0 -> Salir del programa\n"
                              "Escogiendo la herramienta: ")
    # Tablas de Verdad
    if menuprincipal == "1":
        # Se implementa un ciclo for para darle una mejor presentacion.
        for i in range(0, 20):
            print("")

        # Bienvenida
        print(
            "-------------Bienvenido al generador de tablas de verdad-------------\n\n"
            "Explicación breve de la sintaxis:\n"
            "CONJUNCIÓN           -> &\n"
            "DISYUNCIÓN           -> |\n"
            "DISYUNCIÓN EXCLUSIVA -> ^\n"
            "NEGACIÓN             -> !\n"
            "IMPLICACIÓN          -> >\n"
            "DOBLE IMPLICACIÓN    -> <\n\n"
            "°Si deseas salir escribe 'SALIR'.\n"
            "°Te recomendamos abrir el PDF para aprovechar al máximo el programa.")

        # Ciclo while para que siempre se mantenga dentro hasta que escriba la palabra clave
        while True:
            # Solicitamos que ingrese la expresion y la convertimos a mayusculas para que todas las expresiones sean validas.
            x = input("\n\nIngresa tu expresión: ").upper()
            # Cabe la posibilidad de romper el ciclo.
            if x == "SALIR":
                break
            # Abrimos una lista para almacenar todos los datos necesarios.
            variables = []
            # Ciclo for dentro de la cadena 'x'
            for i in x:
                # Imprimimos el ciclo separado por espacio
                print(i, end=' ')
                # Colocamos un if para saber si lo que escribió el usuario es correcto y agregarlo a la lista 'variables'
                if i.isalpha() and not i in variables:
                    variables.append(i)
                    # Agregamos un ciclo for con el tamaño de variables elevado al cuadrado
            for i in range(2 ** len(variables)):
                print('')

                cadena = bin(i)[2:].rjust(len(variables), '0')
                # A partir de 'cadena', la variable 'booleano' arrojará si es verdadero o falso.
                booleano = list(map((lambda x: True if x == '1' else False), cadena))
                # la variable 'a' ocasiona que junte los valores de 'variables' y el resultado de 'booleanos'.
                a = dict(zip(variables, booleano))
                # Creamos la lista 'calculo' para realizar adjuntar todos los datos necesarios que se crearán dentro de las siguientes lineas de codigo
                calculo = []
                # Se crea el ciclo j dentro del ciclo i a partir de x.
                for j in x:
                    # Ingresamos todos los condicionales.
                    if j.isalpha():
                        calculo.append(a[j])
                        print(int(a[j]), end=' ')
                    elif j == '&':
                        calculo[-2] = calculo[-2] & calculo[-1]
                        print(int(calculo[-2]), end=' ')
                        del calculo[-1]
                    elif j == '|':
                        calculo[-2] = calculo[-2] | calculo[-1]
                        print(int(calculo[-2]), end=' ')
                        del calculo[-1]
                    elif j == '^':
                        calculo[-2] = calculo[-2] ^ calculo[-1]
                        print(int(calculo[-2]), end=' ')
                        del calculo[-1]
                    elif j == '>':
                        calculo[-2] = calculo[-2] <= calculo[-1]
                        print(int(calculo[-2]), end=' ')
                        del calculo[-1]
                    elif j == '<':
                        calculo[-2] = calculo[-2] >= calculo[-1]
                        print(int(calculo[-2]), end=' ')
                        del calculo[-1]
                    elif j == '!' or j == '~':
                        calculo[-1] = not calculo[-1]
                        print(int(calculo[-1]), end=' ')
                    # Le aclaramos que no es una expresion valida
                    else:
                        print("Error: Vuelve a intentarlo")
    # Conjuntos
    if menuprincipal == "2":
        # Se implementa un ciclo for para darle una mejor presentacion
        for i in range(0, 20):
            print("")

        # Texto de bienvenida al programa
        print("----------Bienvenido a la calculadora de operaciones sobre conjuntos----------\n"
              "\t\nEn este programa podras hacer 4 tipos de operaciones para manipular conjuntos"
              "\n1: Unión"
              "\n2: Intersección"
              "\n3: Diferencia"
              "\n4: Diferencia Simétrica")

        # Se implementa un ciclo while true para que se pueda repetir el ciclo en caso de que el usuario lo desee
        while True:
            # Se pide cada conjunto como tal
            stringConjuntoA = input("\nIntroduce los valores del conjunto A separados por comas: ")
            stringConjuntoB = input("Introduce los valores del conjunto B separados por comas: ")
            stringConjuntoC = input("Introduce los valores del conjunto C separados por comas: ")
            listaConjuntoA = stringConjuntoA.split(",")
            listaConjuntoB = stringConjuntoB.split(",")
            listaConjuntoC = stringConjuntoC.split(",")

            # Las listas creadas anteriormente se convierten en conjuntos
            conjuntoA = set(listaConjuntoA)
            conjuntoB = set(listaConjuntoB)
            conjuntoC = set(listaConjuntoC)

            # Validación de la longitud y sintaxis de los conjuntos por medio de un ciclo while
            while "" in conjuntoA or "" in conjuntoB or "" in conjuntoC:
                print("\nUno de los conjuntos no es válido, vuelve a introducirlo\n"
                      "--------------------------------------------------------")
                # Se pide cada conjunto como tal
                stringConjuntoA = input("\nIntroduce los valores del conjunto A separados por comas: ")
                stringConjuntoB = input("Introduce los valores del conjunto B separados por comas: ")
                stringConjuntoC = input("Introduce los valores del conjunto C separados por comas: ")
                listaConjuntoA = stringConjuntoA.split(",")
                listaConjuntoB = stringConjuntoB.split(",")
                listaConjuntoC = stringConjuntoC.split(",")
                # Las listas creadas anteriormente se convierten en conjuntos
                conjuntoA = set(listaConjuntoA)
                conjuntoB = set(listaConjuntoB)
                conjuntoC = set(listaConjuntoC)
            print("\n*Los conjuntos son válidos*")

            # Impresión de cada conjunto
            print("\nValores del conjunto A: ", conjuntoA)
            print("Valores del conjunto B: ", conjuntoB)
            print("Valores del conjunto C: ", conjuntoC)

            # Se calcula la cardinalidad por simplemente imprimir la longitud de cada conjunto
            print("\nLa cardinalidad del conjunto A es de: ", len(conjuntoA))
            print("La cardinalidad del conjunto B es de: ", len(conjuntoB))
            print("La cardinalidad del conjunto C es de: ", len(conjuntoC))


            # Función que determina la elección del primer conjunto a elegir para las operaciones
            def eleccion_conjunto1(conjuntoA, conjuntoB, conjuntoC):
                eleccion1 = input("\nElige el primer conjunto sobre el cual quieras operar (A,B o C): ")
                eleccion1 = eleccion1.upper()
                # Se valida la elección del conjunto 1
                while eleccion1 not in "ABC":
                    eleccion1 = input("**No introdujiste correctamente el conjunto a operar**\n\n"
                                      "Elige el primer conjunto sobre el cual quieras operar (A,B o C): ")
                    eleccion1 = eleccion1.upper()
                if eleccion1 == "A":
                    eleccion1 = conjuntoA
                elif eleccion1 == "B":
                    eleccion1 = conjuntoB
                elif eleccion1 == "C":
                    eleccion1 = conjuntoC
                return eleccion1


            # Función que determina la elección del segundo conjunto a elegir para las operaciones
            def eleccion_conjunto2(conjuntoA, conjuntoB, conjuntoC):
                eleccion2 = input("Elige el segundo conjunto sobre el cual quieras operar (A,B o C): ")
                eleccion2 = eleccion2.upper()
                # Se valida la eleccion del conjunto 2
                while eleccion2 not in "ABC":
                    eleccion2 = input("**No introdujiste correctamente el conjunto a operar**\n\n"
                                      "Elige el segundo conjunto sobre el cual quieras operar (A,B o C): ")
                    eleccion2 = eleccion2.upper()
                if eleccion2 == "A":
                    eleccion2 = conjuntoA
                elif eleccion2 == "B":
                    eleccion2 = conjuntoB
                elif eleccion2 == "C":
                    eleccion2 = conjuntoC
                return eleccion2


            # Se le asignan variables a cada función y se imprimen
            eleccion1 = (eleccion_conjunto1(conjuntoA, conjuntoB, conjuntoC))
            eleccion2 = (eleccion_conjunto2(conjuntoA, conjuntoB, conjuntoC))
            print("\nHas seleccionado:\n\t1: ", eleccion1, "\n\t2: ", eleccion2)


            # Se define una función individual para cada tipo de operación
            def union(eleccion1, eleccion2):
                operacion_union = (eleccion1 | eleccion2)
                return operacion_union


            def interseccion(eleccion1, eleccion2):
                operacion_interseccion = (eleccion1 & eleccion2)
                return operacion_interseccion


            def diferencia(eleccion1, eleccion2):
                operacion_dif = (eleccion1 - eleccion2)
                return operacion_dif


            def diferencia_sim(eleccion1, eleccion2):
                operacion_difsim = (eleccion1 ^ eleccion2)
                return operacion_difsim


            print("\n-----------OPERACIONES-----------"
                  "\n1.- Unión --------------------- |"
                  "\n2.- Intersección -------------- &"
                  "\n3.- Diferencia ---------------- -"
                  "\n4.- Diferencia Simétrica ------ ^"
                  "\n5.- Todas --------------------- +"
                  "\nIngresa el número o el símbolo de la operación.")

            # Se elige la operación a realizar con los conjuntos seleccionados
            operacion = input("\nElige una operación para realizar con los conjuntos: ")
            operacion = operacion.upper()
            # Se valida la entrada de la operación
            while operacion not in "12345|&-^+UIT":
                operacion = input("**No ingresaste correctamente la operación, vuelve a intentarlo**\n\n"
                                  "Elige una operación para realizar con los conjuntos: ")
                operacion = operacion.upper()
            # Se implementa una condición por cada tipo de operación
            if operacion[0] == "U" or operacion == "1" or operacion == "|":
                print("\tSeleccionaste: Unión =>", union(eleccion1, eleccion2))
            elif operacion[0] == "I" or operacion == "2" or operacion == "&":
                if interseccion(eleccion1, eleccion2) != set():
                    print("\tSeleccionaste: Intersección =>", interseccion(eleccion1, eleccion2))
                else:
                    print("\tNo hay intersección entre los conjuntos seleccionados")
            elif operacion == "3" or operacion == "-":
                if diferencia(eleccion1, eleccion2) != set():
                    print("\tSeleccionaste: Diferencia =>", diferencia(eleccion1, eleccion2))
                else:
                    print("\tNo hay diferencia entre los conjuntos seleccionados.")
            elif operacion == "4" or operacion == "^":
                if diferencia_sim(eleccion1, eleccion2) != set():
                    print("\tSeleccionaste: Diferencia Simétrica =>", diferencia_sim(eleccion1, eleccion2))
                else:
                    print("\tNo hay diferencia simétrica entre los conjuntos")
            elif operacion[0] == "T" or operacion == "5" or operacion == "+":
                print("\nSeleccionaste todas:")
                print("\tUnión =>", union(eleccion1, eleccion2))
                if interseccion(eleccion1, eleccion2) != set():
                    print("\tIntersección =>", interseccion(eleccion1, eleccion2))
                else:
                    print("\tNo hay intersección entre los conjuntos seleccionados")
                if diferencia(eleccion1, eleccion2) != set():
                    print("\tDiferencia =>", diferencia(eleccion1, eleccion2))
                else:
                    print("\tNo hay diferencia entre los conjuntos.")
                if diferencia_sim(eleccion1, eleccion2) != set():
                    print("\tDiferencia Simétrica =>", diferencia_sim(eleccion1, eleccion2))
                else:
                    print("\tNo hay diferencia simétrica entre los conjuntos seleccionados")

            # La variable repetir se usa para ver si el usuario desea reiniciar el programa
            repetir = input(("\nPrograma terminado.\n"
                             "¿Desea volver a comenzar el programa?\n"
                             "Ingresar un 1 -> Si\n"
                             "Ingresar un 0 -> No\n"
                             "Eligiendo: "))
            while repetir not in "10":
                print("\nNo es una opción correcta, ingresala de nuevo...\n")
                repetir = input(("\nPrograma terminado.\n"
                                 "¿Desea volver a comenzar?\n"
                                 "Ingresar un 1 -> Si\n"
                                 "Ingresar un 0 -> No\n"
                                 "Eligiendo: "))
            if repetir == "1":
                continue
            elif repetir == "0":
                print("\nVolviendo al menú princiapl...")
                break
    # Sucesiones
    if menuprincipal == "3":
        # Limpieza de codigo
        for i in range(0, 20):
            print("")

        # Bienvenida
        print("\n----------Bienvenido a la calculadora de sucesiones--------\n"
              "\nEsta calculadora arroja tres resultados:"
              "\n1. Resultado de cada término de la sucesión"
              "\n2. La sumatoria de la sucesión"
              "\n3. El producto de la sucesión\n"
              "\nPara ingresar tu fórmula, usa la letra 'n' para su sintaxis, y escribela normalmente"
              "\n+ -> suma"
              "\n- -> resta"
              "\n* -> multiplicación"
              "\n/ -> división"
              "\n** -> elevación a una potencia"
              "\nRecuerda usar de manera correcta la jerarquía de operaciones")

        # Ciclo repetitivo para mantener el programa
        while True:
            # Variable formula para ingresar la sucesión como tal, como un string
            formula = str(input("\nIntroduce la fórmula a utilizar -> "))
            # Ciclo mientras no esté letra "n"
            while not "n" in formula:
                print("Vuelve a introducir la fórmula usando 'n' en la misma")
                formula = str(input("\nIntroduce la fórmula a utilizar -> "))
            formula = formula.lower()

            # Se piden los límites inferiores y superiores para la sucesión
            inferior = int(input("Introduce el límite inferior -> "))
            superior = int(input("Introduce el límite superior -> "))
            # Ciclo mientras para comparar los limites y no sean introducidos al revés
            while not inferior < superior:
                print("\nLímites incorrectos. Vuelve a introducirlos")
                inferior = int(input("Introduce el límite inferior -> "))
                superior = int(input("Introduce el límite superior -> "))

            # Listas vacías de la fórmula y resultados para iterar sobre ellas y hacer las evaluaciones
            lista_formula = []
            resultados = []
            # Variables igualadas a 0 para la sumatoria y el producto
            sumatoria = 0
            producto = 0

            # Ciclo for para iterar sobre los límites
            for i in range(inferior, superior + 1):
                # Ciclo for para iterar sobre la cadena y reemplazar la 'n' por el valor de la iteración
                for j in formula:
                    if j == "n":
                        # Se crea una nueva variable para la fórmula
                        formulaN = formula.replace("n", str(i))
                # Se añade cada iteración a la lista vacía
                lista_formula.append(formulaN)

            print("\nResultados:")

            # Ciclo for par iterar sobre la lista de fórmulas
            for i in lista_formula:
                # Uso de la función eval para evaluar la cadena de cada iteración
                resultado = eval(i)
                # Se añade cada resultado a la lista de resultados para poder evaluarlos con las funciones recursivas
                resultados.append(resultado)
                # Impresión de los resultados de cada término de la sucesión
                print(i, "=", resultado)


            # Función recursiva de suma
            def sumar(resultados):
                if len(resultados) == 1:
                    return resultados[0]
                else:
                    return resultados[0] + sumar(resultados[1:])

                # Función recursiva de multiplicación


            def multiplicacion(resultados):
                if len(resultados) == 1:
                    return resultados[0]
                else:
                    return resultados[0] * multiplicacion(resultados[1:])


            # Impresión de los resultados de sumatoria y producto
            print("\nLa sumatoria es ->", sumar(resultados))
            print("El producto es ->", multiplicacion(resultados))

            # Variable repetir para ver si el usuario desea seguir ingresando fórmulas
            repetir = input("\nPrograma terminado."
                            "\n¿Desea volver a comenzar?\n"
                            "Ingresar un 1 -> Si\n"
                            "Ingresar un 0 -> No\n"
                            "Eligiendo: ")
            # Ciclo mientras para validar la entrada correcta
            while repetir not in "10":
                print("\nNo es una opción correcta, ingresala de nuevo...\n")
                repetir = input(("\nPrograma terminado.\n"
                                 "¿Desea volver a comenzar?\n"
                                 "Ingresar un 1 -> Si\n"
                                 "Ingresar un 0 -> No\n"
                                 "Eligiendo: "))
            if repetir == "1":
                continue
            elif repetir == "0":
                print("\nVolviendo al menú principal...")
                break

    # Relaciones
    if menuprincipal == "4":
        def reflexiva(pares):
            for x, y in pares:
                if (x, x) not in pares:
                    return 'Falso'
            return 'Verdadero'


        def simetrica(pares):
            for x, y in pares:
                if (y, x) not in pares:
                    return 'Falso'
            return 'Verdadero'


        def transitiva(pares):
            for x, y in pares:
                for a, b in pares:
                    if y == a and ((x, b) not in pares):
                        return 'Falso'
            return 'Verdadero'


        # Se implementa un ciclo for para darle una mejor presentacion
        for i in range(0, 20):
            print("")

        # Texto de bienvenida al programa
        print("----------Bienvenido a la herramienta de Relaciones y Funciones----------\n"
              "\t\nEn este programa podras ingresar pares ordenados y podrás determinar:"
              "\na) Si es reflexiva"
              "\nb) Si es simetrica"
              "\nc) Si es transitiva")

        # Ciclo para reiniciar programa
        while True:
            # Numero de pares
            cantidad = int(input("\t¿Cuántos pares deseas comparar? -> "))
            # Declaramos variables
            pares, x, y = [], 0, 0
            dominio = []
            codominio = []

            print("\n\tEscribe el par de la siguiente manera: x,y\n"
                  "\t------------------------------------------")

            # Almacena pares en formato especial de lista.
            for i in range(cantidad):
                x, y = input("\tIngresa el par #%d  -> " % (i + 1)).split(",")
                pares.append((x, y))

            # Ciclo para conocer el dominio y codominio
            for i, j in pares:
                # Se agregan los valores si no estan.
                if (i not in dominio):
                    dominio.append(i)
                if (j not in codominio):
                    codominio.append(j)
            print("\t------------------------------------------")

            print("La función es reflexiva: ", reflexiva(pares))
            print("La función es simétrica: ", simetrica(pares))
            print("La función es transitiva:", transitiva(pares))

            # Ordena e imprime el dominio y codominio separados por comas
            dominio.sort()
            dominioR = ", ".join(dominio)
            codominio.sort()
            codominioR = ", ".join(codominio)
            print("\n\tDominio: {" + dominioR + "}\n\tRango: {" + codominioR + "}")

            # Convierte la lista de pares en un string
            pares = str(pares)
            # Extrae todo para quedarse simplemente con los valores
            valores = ' '.join(filter(str.isalnum, pares))
            # Los agrega a una lista separados
            valoresLista = valores.split(" ")
            longitud = len(valoresLista)
            contx = 0
            x = []
            y = []

            # Obtiene valores de x a partir de la lista
            for i in range(0, longitud - 1, 2):
                if valoresLista[i] not in x:
                    x.append(valoresLista[i])
                else:
                    # Si alguna x se repite suma cont
                    contx += 1

            # Obtiene valores de y a partir de la lista
            for j in range(1, longitud, 2):
                if valoresLista[j] not in y:
                    y.append(valoresLista[j])
            if contx != 0:
                print("\t-> No es una función")
            else:
                print("\t-> Es una función")

            # Variable repetir para ver si el usuario desea seguir ingresando fórmulas
            repetir = input("\nPrograma terminado."
                            "\n¿Desea volver a comenzar?\n"
                            "Ingresar un 1 -> Si\n"
                            "Ingresar un 0 -> No\n"
                            "Eligiendo: ")
            # Ciclo mientras para validar la entrada correcta
            while repetir not in "10":
                print("\nNo es una opción correcta, ingresala de nuevo...\n")
                repetir = input(("\nPrograma terminado.\n"
                                 "¿Desea volver a comenzar?\n"
                                 "Ingresar un 1 -> Si\n"
                                 "Ingresar un 0 -> No\n"
                                 "Eligiendo: "))
            if repetir == "1":
                continue
            elif repetir == "0":
                print("\nVolviendo al menú principal...")
                break
    # Salida
    if menuprincipal == "0":
        print("\n\n\n---------------------------------------------------"
              "\n¡Gracias por utilizar nuestro programa!"
              "\nRealizado por:"
              "\n\t-Lomelí Gómez Yahir Alejandro"
              "\n\t-Orozco Sanchez Diego Arturo\n\n"
              "-------------El programa ha terminado.-------------")
        break
