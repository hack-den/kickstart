/////////////////////////
// Created by Vaibhav //
///////////////////////

# include <bits/stdc++.h>
using namespace std;

int main() {
  int t;
  cin >> t;

  // loop over test cases
  for (int l = 1; l <=t; l++) {
    int n, b;
    cin >> n; cin >> b;

    // input the houses
    int h[n];
    for (int i=0; i<n; i++) {
      cin >> h[i];
    }

    // sort the houses in ascending order
    sort(h,h+n);

    // compute the answer
    int y = 0;

    for (int p = 0; p < n; p++) {
      if (b >= h[p]) {
        b -= h[p];
        y += 1;
      }
    }

    cout << "Case #" << l << ": " << y << endl;

  }
}
