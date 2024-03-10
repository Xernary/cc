#include <stdio.h>
#include <iostream>
#include <vector>
#include <array>
#include <cstdlib>
#include <algorithm>
#include<bits/stdc++.h>

using namespace std;

void show(const vector<int>* const Q){
  cout << "Q = ";
  for(int el : *Q)
    cout << el << " ";
  cout << endl;
}

int find_subsets(int N, int D, vector<int>* S){
    // SCRIVI QUA IL TUO CODICE
    int start = 0;
    int end = (*S).size() - 1;
    bool found = false;

    sort((*S).begin(), (*S).end());

    
    for(int el : *S)
      //cout << el  << " ";

    while(abs((*S)[start] - (*S)[end]) > D && start < end){
      found = true;
      if(abs((*S)[start] - (*S)[start+1]) < abs((*S)[end] - (*S)[end-1]))
        end--;
      else 
        start++;
      //cout << "CALLED: " << start << ", " << end << endl;
    }
    //cout << "end: " << start << " start: " << end << endl;
    //show(S);
    int result = 0;
    if(found == true) {
      result = abs(end - start) + 1;
      vector<int>::iterator it;
      it = (*S).begin();
      for(int i = start; i <= end; i++)
        (*S).erase(it + start);
    }
  return result;
}

int main(){

     freopen("input2.txt", "r", stdin); // DECOMMENTA QUA SE VUOI LEGGERE DA FILE
     //freopen("output.txt", "w", stdout); // DECOMMENTA QUA SE VUOI SCRIVERE DA FILE
    int T;
    cin >> T;

    while(T--){
        int N, D;
        vector<int> S;

        cin >> N >> D;
        
        for(int i = 0; i < N; i++){
            int x;
            cin >> x;
            S.push_back(x);
        }
        
        vector<int>* Q = new vector<int>(N);
        for(int i = 0; i < N; i++)
          (*Q)[i] = S[i];

        sort((*Q).begin(), (*Q).end());
        //show(Q);

        cout << find_subsets(N, D, Q) + find_subsets(N, D, Q) << endl;
        
        //show(Q);

    }

    return 0;
}
