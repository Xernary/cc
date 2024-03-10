#include <iostream>
#include <stdio.h>
#include <string>
#include <fstream>
#include <vector>

using namespace std;

void calculate_score(int Q, int N, string correct_answers, vector<string> answers){

  vector points(N, 0);
  int p = 0;
  
  for(string s : answers){

    for(int i = 0; i < Q; i++){
      if(s[i] == correct_answers[i])
        points[p] += 1;
    }
    p++;
  }

  for(int i = 0; i < N; i++)
    cout << points[i] << "\n";

}

int main(int argn, char* args[]){

  // read from file
  ifstream file("input-1-0.txt");
 
  int Q, N;
  string correct_answers;

  if(file.is_open()){
      file >> Q >> N;
      file >> correct_answers;
  }

  vector<string> answers(N);
  
  int n = 0;
  if(file.is_open()){
    while(file.good()){
      file >> answers[n];
      n++;
    }
  }
  
  calculate_score(Q, N, correct_answers, answers);


}
