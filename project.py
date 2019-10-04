# Universidad del Valle de Guatemala
# Matematica Discreta - seccion 10
# María Mercedes Retolaza Reyna, 16339
# Archivo: proyect.py
# Fecha: 4/10/2019

#IMPORTANTE: usted ingresa la matriz y le dice que propiedades tiene en conjunto. No evalua propiedad por propiedo

# Para todas las operaciones de matrices
# Se necesita de Numpy
import numpy as np


def validateNum(value):
    # Valida si el ingreso del numero
    # Es un valor correcto
    try:
        int(value)
        return True
    except ValueError:
        return False
# Verifica que el rango sea un valor n=n debido a
# que las matrices que se están trabajando son cuadradas.


def isValueInRange(testValue, num1, num2):
    # Verifica si el test value pertenecen
    # al rango establecido por num1 y num2
    if(testValue >= num1 and testValue <= num2) or (testValue <= num1 and testValue >= num2):
        return True
    return False

# Se declaran las propiedades de
# una MATRIZ DE RELACIÓN
################################################F u n  t i o n s###########################################################################

# Se verifica si es una matriz simétrica
# parametro: una matriz binaria
# retorno: devuelve True si A (intersección) AT (transposición) <= I


def isSymmetric(binaryMatrix):
    # Se usa directo la libreria de np
    return(binaryMatrix.equalsOfMatrix(binaryMatrix.transposedOfMatrix()))

# Se verifica si es reflexiva
# parameto: una matriz binaria
# retorno: devuelve *True* si A = A ** T (matriz transpuesta)


def isReflexive(binaryMatrix):
    # Se calcula la matriz identidad
    # uso de librería de np
    identMatrix = np.identity(binaryMatrix.matrix.shape[0], dtype=int)
    # Se aplica la matriz identidad en la matriz binaria
    identBinary = RelationMatrix(identMatrix)
    # Retorno de resultado final
    return(identBinary.precedenceOfMatrix(binaryMatrix.matrix))

# Se verifica si es una matriz simétrica
# parametro: una matriz binaria
# retorno: devuelve True si A ** 2 <= A


def isAntisymmetric(binaryMatrix):
    # Se calcula la matriz identidad
    identMatrix = np.identity(binaryMatrix.matrix.shape[0], dtype=int)
    # Retorno de resultado final
    # Se aplica la intersección de la matriz transpuesta (composición)
    return((binaryMatrix.intersectionOfMatrix(binaryMatrix.transposedOfMatrix())).precedenceOfMatrix(identMatrix))

# Verifica si una matriz es transitiva
# parametro: una matriz binaria
# retorno: devuelve si es transitiva o no la matriz (su composición es igual)


def isTransitive(binaryMatrix):
    return((binaryMatrix.multiplicationOfMatrix(binaryMatrix.matrix)).precedenceOfMatrix(binaryMatrix.matrix))


class RelationMatrix(object):

    def __init__(self, matrix):
        # Se declara una matriz de np
        self.matrix = matrix

    def transposedOfMatrix(self):
        return self.matrix.transpose()

    def equalsOfMatrix(self, firstMatrix):
        return np.array_equal(self.matrix, firstMatrix)

    def multiplicationOfMatrix(self, firstMatrix):
        # Se realiza producto punto de matrices
        dotProductOfMatrix = np.dot(self.matrix, firstMatrix)
        return (RelationMatrix(dotProductOfMatrix))

    def intersectionOfMatrix(self, firstMatrix):
        # Se valida la interesccion entre matrices
        valueA = np.array(self.matrix, dtype=bool)
        valueB = np.array(firstMatrix, dtype=bool)
        return RelationMatrix(1*np.logical_and(valueA, valueB))

    def precedenceOfMatrix(self, firstMatrix):
        # Se evalua la precedencia de matrices / aun no terminado
        boolMatrix = self.matrix <= firstMatrix
        boolMatrixTest = np.where(boolMatrix == False)[0]
        if(boolMatrixTest.size > 0):
            return False
        # TO-DO
        return True


option = 1

while(option != 2):
    print("\n\t\tPROGRAMA DE MATRICES!\n")
    print("""
		***************************************************
		Seleccione una opción
		1. Ver propiedades de matrices
		2. Terminar el programa
		***************************************************
	""")
    option = input("> ")
    if(validateNum(option)):
        option = int(option)
        validRange = isValueInRange(option, 1, 2)
        if(validRange):
            if(option == 1):
                print("""
				
                _______  .-./`)     .-''-.  ,---.   .--.,---.  ,---.   .-''-.  ,---.   .--..-./`)  ______         ,-----.     
                \  ____  \\ .-.')  .'_ _   \ |    \  |  ||   /  |   | .'_ _   \ |    \  |  |\ .-.')|    _ `''.   .'  .-,  '.   
                | |    \ |/ `-' \ / ( ` )   '|  ,  \ |  ||  |   |  .'/ ( ` )   '|  ,  \ |  |/ `-' \| _ | ) _  \ / ,-.|  \ _ \  
                | |____/ / `-'`"`. (_ o _)  ||  |\_ \|  ||  | _ |  |. (_ o _)  ||  |\_ \|  | `-'`"`|( ''_'  ) |;  \  '_ /  | : 
                |   _ _ '. .---. |  (_,_)___||  _( )_\  ||  _( )_  ||  (_,_)___||  _( )_\  | .---. | . (_) `. ||  _`,/ \ _/  | 
                |  ( ' )  \|   | '  \   .---.| (_ o _)  |\ (_ o._) /'  \   .---.| (_ o _)  | |   | |(_    ._) ': (  '\_/ \   ; 
                | (_{;}_) ||   |  \  `-'    /|  (_,_)\  | \ (_,_) /  \  `-'    /|  (_,_)\  | |   | |  (_.\.' /  \ `"/  \  ) /  
                |  (_,_)  /|   |   \       / |  |    |  |  \     /    \       / |  |    |  | |   | |       .'    '. \_/``".'   
                /_______.' '---'    `'-..-'  '--'    '--'   `---`      `'-..-'  '--'    '--' '---' '-----'`        '-----'     
                                                                                                                                                                               
					Ingresar matriz relación de la siguiente forma:  
					recuerde, colocar un "*" (asterisco) al final para lograr su ejecución. 
                    #IMPORTANTE# --> No evalua propiedad por propiedad; Se evalua en un conjuunto
					> 1 0 1
					> 1 1 1
					> 1 0 0
					> *
				""")

                myFirstMatrix = []
                matrixValueL = input("> ")
                while(matrixValueL != '*'):
                    newRowOfMatrix = matrixValueL.split(' ')
                    myFirstMatrix.append(newRowOfMatrix)
                    matrixValueL = input("> ")

                matrix = np.array(myFirstMatrix, dtype=int)
                matrix = RelationMatrix(matrix)

                # Llamado a las funciones declaradas
                # Se compara si la matrix que ingresa el usuario
                # Contiene alguna de las propiedades indicadas

                isReflexiveMatrix = "SI" if isReflexive(matrix) else "NO"
                isSymmetricMatrix = "SI" if isSymmetric(matrix) else "NO"
                isAntisymmetricMatrix = "Si" if isAntisymmetric(
                    matrix) else "NO"
                isTransitiveMatrix = "SI" if isTransitive(matrix) else "NO"

                print("*****************************")
                print("* Reflexiva: " + isReflexiveMatrix)
                print("* Simétrica: " + isSymmetricMatrix)
                print("* Antisimétrica: " + isAntisymmetricMatrix)
                print("* Transitiva: " + isTransitiveMatrix)
                print("******************************")

            elif(option == 2):  # Salir del orograma
                print("Finl del programa")
        else:
            print('Error, el valor se encuentra fuera del rango')
    else:
        print("Error, el valor ingresado no es un número correcto")
