
r"""Test cases
>>> run_answer() # doctest: +NORMALIZE_WHITESPACE
2014,a,1
2014,b,1
2014,d,2
2014,e,1
2015,a,3
2015,b,1
2015,c,3
2015,d,2
2015,e,2
2016,a,2
2016,b,1
2016,c,3
2016,d,3
2016,e,3
2017,a,1
2017,b,1
2017,c,1
2017,e,1
2018,a,1
2018,d,1
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
