import os
import datetime
distances   = [0.2, 0.1, 0.05, 0.01]
labels      = [0,3,4,7,9]
model_names = ['mnist_test_model_5_30', 'mnist_test_model_8_20',
               'mnist_test_model_6_25']
arch        = [(5,30), (8,20), (6,25)]
percents    = [90, 95, 99]
activations = ['leaky_relu']
techniques  = ['random']

for distance in distances:
    for label in labels:
        for model_name in model_names:
            for activation in activations:
                for percent in percents:
                    for tech in techniques:
                        command = 'python run.py -A ' + tech + ' -N ' + \
                        str(arch[model_names.index(model_name)][1]) + ' -HL ' +\
                        str(arch[model_names.index(model_name)][0]) + ' -C ' +\
                        str(label) + ' -AC ' + activation + ' -D ' +\
                        str(distance) + ' -P ' + str(percent) + ' -M ' + \
                        model_name + ' -LOG experiment/logfile_temp_random.log'

                        start = datetime.datetime.now()
                        os.system(command)
                        end = datetime.datetime.now()
                        logfile = open('experiment/logfile_temp_random.log','a')
                        logfile.write('Total time (including preperations): ' + str(end-start))
                        logfile.close()