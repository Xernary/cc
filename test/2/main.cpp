#include <stdio.h>
#include <iostream>
#include <vector>
#include <array>
#include <map>
#include <stdlib.h>
#include <bits/stdc++.h>
#include <boost/algorithm/string.hpp>

using namespace std;

int get_variable(const char ch){
  return int(ch) - 97;
}

long long emulate(int N, vector<vector<string>> code){
    // SCRIVI QUA IL TUO CODICE
    vector<int> variables(6, 0);
    map<string, int> labels;

    
    for(int i = 0; i < N; i++){
      string command = code[i][0];
      if(command == "add")
        variables[get_variable(code[i][1][0])] += stoi(code[i][2]);  
      else if(command == "mul")
        variables[get_variable(code[i][1][0])] *= stoi(code[i][2]);  
      else if(command == "sub")
        variables[get_variable(code[i][1][0])] -= stoi(code[i][2]);  
      else if(command == "lab"){
        labels.insert({code[i][1], i});
      }
      else if(command == "jmp"){
        if(variables[get_variable(code[i][1][0])] == stoi(code[i][2])){
          auto pos = labels.find(code[i][3]);
          if (pos != labels.end()) 
            i = pos->second;
        }
      }
    } 
    

    long long sum = 0;
    for(int i = 0; i < 6; i++)
      sum += variables[i];

    return sum;
}


int main()
{

     freopen("input.txt", "r", stdin); // DECOMMENTA QUA SE VUOI LEGGERE DA FILE
     freopen("output.txt", "w", stdout); // DECOMMENTA QUA SE VUOI SCRIVERE DA FILE

    int N;
    vector<string> code;
    string s;
    cin >> N;
    getline(cin, s);

    for(int i = 0; i < N; i++){
        getline(cin, s);
        code.push_back(s);
    }

    vector<vector<string>> v(N, vector<string>(20));
    for(int i = 0; i < N; i++){
      boost::split(v[i], code[i], boost::is_any_of(" "));
  }
 

    
    cout << emulate(N, v) << endl;
    

    return 0;
}
