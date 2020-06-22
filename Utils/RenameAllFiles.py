import os
import shutil

file_loc = '/home/saibharadwaj/PycharmProjects/DataInterviewQuestions/Questions/'
files = list(os.listdir(file_loc))
print(files)
files.remove('__init__.py')

for f in files:
    q_num = f[1:f.find('_')]
    q_name = f[f.find('_')+1:]
    new_f = 'Q_{}_{}'.format(str(q_num).zfill(3), q_name)
    print(q_num, '-->', q_name, '-->', file_loc+f, '-->', file_loc+new_f)
    shutil.move(src=file_loc+f, dst=file_loc+new_f)

print(len(files))
print('Done')

