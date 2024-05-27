#! /usr/bin/python3

import datetime
import glob
import os
import os.path
import yaml


def run():
    """Execcute specific grader program for each question in the 
    course directory"""

    ## get the howework directories
    homeworks = sorted(glob.glob('**/', recursive=False))

    ## get the curren directries
    home = os.getcwd()

    for homework in sorted(homeworks):
        homework_dir = home + '/' + homework
        os.chdir(homework_dir)
        questions = glob.glob('**/', recursive=False)
    
        for q in sorted(questions):
            
            title = '   Grading: ' + homework + '/' + q + '   '
            title = 'Grading: ' + homework + '/' + q
            print(title)

            os.chdir(homework_dir + q)
            os.system('python3 grader.py')
    
    os.chdir(home)


def compute_weights():
    """Collect grades and points for each homework"""
    
    grades = {}

    ## get the howework directories
    homeworks = sorted(glob.glob('**/', recursive=False))

    ## grades of the homeworks
    homework_grades = {}

    ## get the curren directries
    home = os.getcwd()

    for homework in sorted(homeworks):

        homework_dir = home + '/' + homework
        os.chdir(homework_dir)
        
        # grades each point in the current homework
        questions = glob.glob('**/', recursive=False)
        grades = {}
        for question_dir in sorted(questions):
            os.chdir(homework_dir + question_dir)
            question_score = int(question_dir[-3:-1])
            question_grade = 5.0 if os.path.isfile(homework_dir + question_dir + '_SUCCESS') else 0.0
            grades[question_dir] = { 
                '_score' : question_score, 
                '_grade' : None,
                'tree' : question_grade 
            }

        homework_score = int(homework_dir[-3:-1])
        homework_grades[homework] = {
            '_score' : homework_score, 
            '_grade' : None,
            'tree' : grades 
        }

    course_grade = {
            '_score' : 100, 
            '_grade' : None,
            'tree' : homework_grades,
            'date' : str(datetime.datetime.now()) 
    }

    os.chdir(home)

    return course_grade



def compute_grades(course_grade):

    def compute(data):

        if  not isinstance(data['tree'], dict):

            data['_grade'] = data['tree']

        else:

            for key in data['tree'].keys():
                data['tree'][key] = compute(data['tree'][key])

            total_score = sum([data['tree'][key]['_score']  for key in data['tree'].keys()])

            grade = 0.0
            for key in data['tree'].keys():
                grade += data['tree'][key]['_grade'] *  data['tree'][key]['_score'] / total_score
            
            data['_grade'] = round(grade, 2)

        return data

    return compute(course_grade)


def remove_success():
    homeworks = sorted(glob.glob('**/', recursive=False))
    home = os.getcwd()
    for homework in sorted(homeworks):
        homework_dir = home + '/' + homework
        os.chdir(homework_dir)
        questions = glob.glob('**/', recursive=False)
        for question_dir in sorted(questions):
            os.chdir(homework_dir + question_dir)
            if os.path.isfile(homework_dir + question_dir + '_SUCCESS'):
                os.remove(homework_dir + question_dir + '_SUCCESS')    
    os.chdir(home)



run()
course_grades = compute_weights()
course_grades = compute_grades(course_grades)
remove_success()
with open('grade.yaml', 'wt') as f:
    yaml.dump(course_grades, f)
    print(datetime.datetime.now(), file=f)

print(yaml.dump(course_grades))