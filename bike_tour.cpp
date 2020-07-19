/////////////////////////
// Created by Vaibhav //
///////////////////////

# include <bits/stdc++.h>

using namespace std;

int main() {
  int t,l;
  cin >> t;
  for (l = 1; l <= t; l++) {
    int n,y = 0;
    cin >> n;
    int c[n];

    // input the integers
    for (int i = 0; i < n; i++) {
      cin >> c[i];
    }

    for (int l = 1; l < n; l++) {
      if (c[l] > c[l-1] and c[l] > c[l+1]) {
        y += 1;
      }
    }

    // print the answer in Google Kickstart format
    cout << "Case #" << l << ": " << y << endl;
  }

}
