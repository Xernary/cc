#include <stdlib.h>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <iostream>
#include <tuple>
#include <fstream>

using namespace std;

void calculate_scoreboard(int M, int N, int S, 
                     map<int, pair<string, int>> tasks,  
                     vector<tuple<int, int, string, int>> submissions){

  vector<vector<int>> scores(M, vector<int>(N, 0));
  vector<vector<int>> times(M, vector<int>(N, 0));
  vector<vector<int>> scoreboard(M, vector<int>(3, 0));
  vector<tuple<int, int, int>> players(M, make_tuple(0, 0, 0));

  int times_sum = 0;
  int scores_sum = 0;

  for(int i = 0; i < M; i++){
    scoreboard[i][2] = -(i+1);    
  }

  for(int i = 0; i < S; i++){
    
    int player = get<0>(submissions[i]);
    int task = get<1>(submissions[i]);

    // check to see if valid submission
    if((get<2>(submissions[i]) == get<0>(tasks[task-1])) 
       && times[player-1][task-1] == 0 
       || times[player-1][task-1] > get<3>(submissions[i])){
      scores[player-1][task-1] = get<1>(tasks[task-1]); 
      times[player-1][task-1] = get<3>(submissions[i]); 
    }
  }

  for(int i = 0; i < M; i++){
    scores_sum = 0;
    for(int j = 0; j < N; j++){
      scores_sum += scores[i][j];
    }
    scoreboard[i][0] = scores_sum;
  }

  for(int i = 0; i < M; i++){
    scoreboard[i][1] = *max_element(times[i].begin(), times[i].end());
  }
  
  sort(scoreboard.begin(), scoreboard.end());
  reverse(scoreboard.begin(), scoreboard.end());

  for(int i = 0; i < M; i++){
    cout << -scoreboard[i][2] << " " << scoreboard[i][0] << "\n"; 
  }

}

int main(int argn, char* args[]){

  // read from file
  ifstream file("input-1-0.txt");
 
  int M, N, S;
  map<int, pair<string, int>> tasks;

  if(file.is_open()){
      file >> M >> N >> S;
      string b;
      int a, c;
      for(int i = 0; i < N; i++){
        file >> a >> b >> c;
        tasks[i] = make_pair(b, c);
    }
  }

  vector<tuple<int, int, string, int>> submissions(S);
  
  int n = 0;
  if(file.is_open()){
    while(n < S){
      int a, b, d;
      string c;
      file >> a >> b >> c >> d;
      submissions[n] = make_tuple(a, b, c, d);
      n++;
    }
  }

  calculate_scoreboard(M, N, S, tasks, submissions);
}

