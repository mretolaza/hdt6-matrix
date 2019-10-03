# Universidad del Valle de Guatemala
# Matematica Discreta - seccion 10
# María Mercedes Retolaza Reyna, 16339
# Archivo: proyect.py
# Fecha: 4/10/2019


# Para todas las operaciones de matrices
# Se necesita de Numpy
import numpy as np

def validateNumber(variable):
    try:
        # Try cast
        int(variable)
        return True
    except ValueError:
        return False


def isOptionInRange(x, a, b):
    # Validates range
    if(x >= a and x <= b) or (x <= a and x >= b):
        return True
    return False


# MATRIX RELATION PROPERTIES UTILS
def isReflexive(binaryMatrix):
    identityMatrix = np.identity(binaryMatrix.matrix.shape[0], dtype=int)
    identityBinary = BinaryRelationMatrix(identityMatrix)
    return(identityBinary.precedence(binaryMatrix.matrix))

# Returns True if A = A**T (transposed)


def isSymmetric(binaryMatrix):
    return(binaryMatrix.equals(binaryMatrix.transposed()))

# Retuns True if	A (intersection) A**T (transposed) <= I


def isAntisymmetric(binaryMatrix):
    # Calculate Identity Matrix
    identityMatrix = np.identity(binaryMatrix.matrix.shape[0], dtype=int)
    return((binaryMatrix.intersection(binaryMatrix.transposed())).precedence(identityMatrix))

# Returns True if A**2 <= A


def isTransitive(binaryMatrix):
    return((binaryMatrix.multiplication(binaryMatrix.matrix)).precedence(binaryMatrix.matrix))

# Class for relation matrix management


class BinaryRelationMatrix(object):

    def __init__(self, matrix):
        # Numpy matrix
        self.matrix = matrix

    def multiplication(self, inputMatrix):
        dotMatrix = np.dot(self.matrix, inputMatrix)
        return (BinaryRelationMatrix(dotMatrix))

    def intersection(self, inputMatrix):
        a = np.array(self.matrix, dtype=bool)
        b = np.array(inputMatrix, dtype=bool)
        return BinaryRelationMatrix(1*np.logical_and(a, b))

    def precedence(self, inputMatrix):
        booleanMatrix = self.matrix <= inputMatrix
        booleanMatrixSearch = np.where(booleanMatrix == False)[0]
        if(booleanMatrixSearch.size > 0):
            return False
        # Not implemented yet
        return True

    def transposed(self):
        return self.matrix.transpose()

    def equals(self, inputMatrix):
        return np.array_equal(self.matrix, inputMatrix)


option = 1

while(option != 2):
    print("\n\t\tWELCOME!\n")
    print("""
		----------------------------
		Choose an option:
		1. Show relation matrix properties
		2. Exit
		----------------------------
	""")
    option = input("> ")
    if(validateNumber(option)):
        option = int(option)
        # Check if option is in range
        validRange = isOptionInRange(option, 1, 2)
        if(validRange):
            if(option == 1):  # Check Matrix properties
                print("""
				
                    .-------.        .-''-.     .-'''-.   ___    _   .---. ,---------.  
                    |  _ _   \     .'_ _   \   / _     \.'   |  | |  | ,_| \          \ 
                    | ( ' )  |    / ( ` )   ' (`' )/`--'|   .'  | |,-./  )  `--.  ,---' 
                    |(_ o _) /   . (_ o _)  |(_ o _).   .'  '_  | |\  '_ '`)   |   \    
                    | (_,_).' __ |  (_,_)___| (_,_). '. '   ( \.-.| > (_)  )   :_ _:    
                    |  |\ \  |  |'  \   .---..---.  \  :' (`. _` /|(  .  .-'   (_I_)    
                    |  | \ `'   / \  `-'    /\    `-'  || (_ (_) _) `-'`-'|___(_(=)_)   
                    |  |  \    /   \       /  \       /  \ /  . \ /  |        \(_I_)    
                    ''-'   `'-'     `'-..-'    `-...-'    ``-'`-''   `--------`'---'    
                                                                    
					Ingresar matriz relación de la siguiente forma:  
					recuerde, colocar un "*" al final para lograr su ejecución
					> 1 0 1
					> 1 1 1
					> 1 0 0
					> *
				""")

                myRelationMatrix = []
                matrixLine = input("> ")
                while(matrixLine != '*'):
                    newRow = matrixLine.split(' ')
                    myRelationMatrix.append(newRow)
                    matrixLine = input("> ")

                matrix = np.array(myRelationMatrix, dtype=int)
                matrix = BinaryRelationMatrix(matrix)

                # Checking properties
                isReflexiveMatrix = "Yes" if isReflexive(matrix) else "No"
                isSymmetricMatrix = "Yes" if isSymmetric(matrix) else "No"
                isAntisymmetricMatrix = "Yes" if isAntisymmetric(
                    matrix) else "No"
                isTransitiveMatrix = "Yes" if isTransitive(matrix) else "No"

                print("*****************************")
                print("* Reflexivity: " + isReflexiveMatrix)
                print("* Symmetry: " + isSymmetricMatrix)
                print("* Antisymmetry: " + isAntisymmetricMatrix)
                print("* Transitivity: " + isTransitiveMatrix)
                print("******************************")

            elif(option == 2):  # Exit
                print("Exit...")
        else:
            print('Value out of range, try again...')
    else:
        print("Value is not a valid number, try again...")
