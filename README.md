# shift_work_schedule
generator of the shift work schedule using random method  

This code helps a work group arrange its shift work schedule easily.  
By setting the conditions needed in the score part,  
we can get the schedule with the highest score for usage. 

How to use the code: 
1. Modify the work duty in the w_schedule_in.csv 
   
   Example:
   ------------ Carl   Mary   Tim     Amy  
   Morning       1      1      0       0 ---> duty off  
   Afternoon     0      0      1       1 ---> duty on   
                 17            25---> Friday Afternoon leave  
                 |             |  
                 Sunday morning leave  
2. Entering the command: python3 schedule_gen.py  
3. Check the output in w_schedule_out.csv  

Future works:  
Make more complicated score rules for practical usage.
