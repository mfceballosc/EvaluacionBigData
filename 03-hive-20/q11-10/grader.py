
r"""Test cases
>>> run_answer() # doctest: +NORMALIZE_WHITESPACE
E,3,5
A,3,4
B,4,4
A,2,4
C,4,4
A,2,5
A,3,6
B,2,3
E,4,6
B,4,6
C,4,5
C,4,3
D,4,5
E,2,3
B,2,5
D,2,4
E,3,6
D,2,3
E,4,3
E,2,3
E,2,3
E,3,3
D,3,3
A,3,5
E,2,6
E,3,6
A,3,3
E,3,5
A,2,5
C,4,6
A,2,5
D,2,6
E,2,4
B,3,6
B,3,5
D,2,3
B,2,5
C,4,3
E,2,3
E,3,3
<BLANKLINE>

"""
import doctest
import subprocess
import os

def run_answer():
    '''Codigo especifico para ejecutar la respuesta'''
    #----------------------------------------------------------------------------------------------
    # Ejecuta el código del estudiante
    #----------------------------------------------------------------------------------------------
    result = os.popen('hive -S -e "source question.hql"').read()
    result = os.popen('cat output/*').read()
    print(result)

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
