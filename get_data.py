import pandas as pd
from connect import connect
import time, datetime

def run_script(iteration = 1):
    counter = []
    delay = []
    for a in range(iteration):
        start_time = time.time()
        connect()
        execution_time = (time.time() - start_time)
        print('Time to run the main Python script: ' + str(execution_time))
        counter.append(a)
        delay.append(execution_time)
    # name of csv file
    filename = "delay_file_friday_18.csv"

    # dictionary of lists  
    dict = {'count': counter, 'delay': delay}  
    df = pd.DataFrame(dict) 

    # saving the dataframe 
    df.to_csv(filename) 


if __name__ == '__main__':
    run_script(200)