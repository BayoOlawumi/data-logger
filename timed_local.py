import pandas as pd
from connect import connect
import time, datetime

def run_script_local():
    print("Execution Started :",datetime.datetime.now())
    counter = []
    execution_p = []
    id = []
    code_start = time.time()
    web_timestamp = []
    arrived_time = []
    while(True):
    	start_time = time.time()
    	data = connect('streaming')
    	execution_time = (time.time() - start_time)
    	print('Time to run the main Python script: ' + str(execution_time))
    	arrived_time.append(datetime.datetime.now())
    	id.append(data[0])
    	web_timestamp.append(data[1] + datetime.timedelta(hours=2))
    	execution_p.append(execution_time)
    	#After 5 minutes
    	if time.time() - code_start > 300:
    		break
    # name of csv file
    filename = "timed_streaming.csv"

    # dictionary of lists  
    dict = {'id': id,'web-timestamp': web_timestamp, 'arrival-time': arrived_time, 'query-execution-time': execution_p}  
    df = pd.DataFrame(dict) 

    # saving the dataframe 
    df.to_csv(filename) 
    print("Execution Ended :",datetime.datetime.now())

if __name__ == '__main__':
    run_script_local()
