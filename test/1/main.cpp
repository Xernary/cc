#include <stdio.h>
#include <iostream>
#include <vector>
#include <array>
#include <string>

using namespace std;

vector<string> sanitize(int N, int M, vector<string> words, vector<string> banned){
    vector<string> answers(N, "SAFE");
    // SCRIVI QUA IL TUO CODICE
    
    for(int i = 0; i < N; i++){
      for(int j = 0; j < M; j++){
        bool is_banned = words[i].find(banned[j]) != string::npos;
        if(is_banned == true){
          answers[i] = "BANNED";
          break;
        }
      }
    }

    return answers;
}

int main()
{

     freopen("input.txt", "r", stdin); // DECOMMENTA QUA SE VUOI LEGGERE DA FILE
     freopen("output.txt", "w", stdout); // DECOMMENTA QUA SE VUOI SCRIVERE DA FILE

    int N, M;
    vector<string> words, banned, answers;
    cin >> N >> M;

    for(int i = 0; i < M; i++){
        string s;
        cin >> s;
        banned.push_back(s);
    }

    for(int i = 0; i < N; i++){
        string s;
        cin >> s;
        words.push_back(s);
    }

    answers = sanitize(N, M, words, banned);

    for(auto s : answers){
        cout << s << endl;
    }

    return 0;
}
