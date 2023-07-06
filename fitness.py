# activities={"running":10,"swimming":8,"cycling":6}
# activities_done={}
# total_cal_burned=0
# activity=""
# while activity!='done for the day':
#     activity=input("enter the activity you have done today:")
#     for exercise,cal_burn in activities.items():
#         if activity==exercise:
#             time_consumed=float(input("enter how much time in minutes:"))
#             activities_done[exercise]=time_consumed
#             total_cal_burned=float(total_cal_burned)+int(cal_burn)*time_consumed
# print("Here is your activity summury")
# print(activities_done)
# print("Total calorie burned:",str(total_cal_burned))       


def cal_burned(activity,time_consumed):
    chart={"running":10,"swimming":15,"cycling":12}
    activities_done={}
    total_time_consumed=0
    # while activity!='done':
    #     activity=input("enter the activity you have done today or (enter'done' to finish)")
    for exercise,calorie in chart.items():
            if activity==exercise:
                # time_consumed=int(input('total time taken while doing the exercise:'))
                activities_done[activity]=time_consumed
                total_time_consumed=int(total_time_consumed)+int(time_consumed)*int(calorie)
    return activities_done,total_time_consumed    
total_time_consumed, activities_done=cal_burned(activity="swimming", time_consumed=15)
print(total_time_consumed)
print(activities_done)








    























    


