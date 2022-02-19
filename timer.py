import threading
import 

def time_operation():
    timer = threading.Timer(5000,)
	
    
    
    # name of csv file
    filename = "timed_streaming.csv"

    # dictionary of lists  
    dict = {'id': id,'web-timestamp': web_timestamp, 'arrival-time': arrived_time, 'query-execution-time': execution_p}  
    df = pd.DataFrame(dict) 

    # saving the dataframe 
    df.to_csv(filename) 
    print("Execution Ended :",datetime.datetime.now())
    
    

