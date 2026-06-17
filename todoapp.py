data = ["hello","hi"]
def add_task():
      new_task = input("-")
      data.append(new_task)

def view_task():
   for i in data:
      print(i)
   
def delete_task():

   for index, task in enumerate(data):
      print(index+1, task)
      delete_task = input("number of the task to delete")
      data.remove(delete_task-1)
      
while(True):
  instruction = input("""
1)Add task
2)View tasks
3)Complete task
4)Delete tsk                 
5)Exit
 
press any number to continue                      
  """)
  

  

  if instruction =="1" :
    print("add a new task")
    add_task()
  elif instruction =="2":
    if len(data) == 0:
       print("no task found")
    else:
       view_task()
  elif instruction =="3":
    print("completed tasks")  
  elif instruction =="4":
    print("select tasks to delete") 
    delete_task()
  elif instruction =="5":
    print("exited")
    break
   
  else:
    print("invalid number")

