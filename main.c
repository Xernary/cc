#include <stdlib.h>
int check_workers(int workers_number, const int workers[workers_number]){
  for(int i = 0; i < workers_number; i++) 
    if(workers[i] != 0) return 0;
  return 1;
}

int main(int argn, char* args[argn]){

  if(argn < 3) return 0;

  int total_tasks = atoi(args[0]);
  int total_time = atoi(args[1]);
  int tasks_times[argn - 2];
  int workers[50];

  for(int i = 0; i < argn - 2; i++){
    tasks_times[i] = atoi(args[i+2]);
  }

  int workers_number = 0;
  int remaining_time = total_time;
  int queue_size = total_tasks;

  while(queue_size =! 0 || check_workers(workers_number, workers) != 1){
    workers_number++;
    queue_size = total_tasks;
      for(int i = 0; i < workers_number; i++)
        workers[i] = 0;
      for(int i = 0; i < workers_number && i < total_tasks; i++)
        workers[i] = tasks_times[i]; 

    int next_task = 0;
    while(remaining_time >= 0){

      int min[2];
      min[0] = 0;
      min[1] = workers[0];
      for(int i = 0; i < workers_number; i++){
        if(min[1] < workers[i]){
          min[0] = 1;
          min[1] = workers[i];
        } 
      }
      for(int i = 0; i < workers_number; i++)
        workers[i] -= min[1];
      remaining_time -= min[1];
      
      if(next_task >= total_tasks){
        for(int i = 0; i < workers_number; i++)
         workers[i] -= remaining_time;
        break;
      }else{
      workers[min[0]] += tasks_times[next_task];
      }
      next_task++;
      queue_size--;
    } 
  }



    
}
