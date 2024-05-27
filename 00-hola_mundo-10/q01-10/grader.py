#! python3
r"""Test cases
>>> run_answer()
Hola mundo!

"""
import doctest
import subprocess

def run_answer():
    '''Codigo especifico para ejecutar la respuesta'''
    #----------------------------------------------------------------------------------------------
    # Ejecuta el código del estudiante
    #----------------------------------------------------------------------------------------------
    answer = open('question.py', 'rt', encoding='utf-8').readlines()
    answer = [row for row in  answer if len(row) >= 2 and row[0:2] != '##']
    answer = '\n'.join(answer)
    return exec(answer)

#--------------------------------------------------------------------------------------------------
# Grader (generic)
#--------------------------------------------------------------------------------------------------
subprocess.run(['rm', '-f', '_SUCCESS']) # borra el flag de exito de la corrida
RESULT = doctest.testmod()               # ejecuta el doctest
FAIL, _ = RESULT                         # fail, total
if FAIL == 0:                            # grading
    open('_SUCCESS', 'a').close()        #
else:
    print('\n')
#--------------------------------------------------------------------------------------------------
