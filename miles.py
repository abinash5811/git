total_time=0
mile_count=0
value=""
while value!="done":
    value=input('enter the time it took to run each mile(type"done" to exit):')
    if value!="done":
        if float(value)>0:
            time_for_each_lap=float(value)
            total_time+=time_for_each_lap
            mile_count+=1
        else:
            print("please enter a positive integer")
if mile_count>0:
    avg_pace=total_time/mile_count
    print(f"your avg. pace is {avg_pace:.2f} minutes per mile")   
else:
    print("no miles were entered")                 
