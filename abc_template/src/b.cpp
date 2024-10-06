/**
 * @file    b.cpp
 * @brief   This program is a template.
 * @author  tatsujin
 * @date    xxxx-yy-zz
 */

#include <bits/stdc++.h>
using namespace std;

int main() {
  // input
  int n;
  cin >> n;
  vector<int> a(n);
  for (auto &e : a) {
    cin >> e;
  }

  int answer = 0;
  while (true) {
    // sort
    sort(a.begin(), a.end(), greater<int>());

    // check condition
    if (a[0] == 0 || a[1] == 0) {
      break;
    }

    // apply
    a[0] -= 1;
    a[1] -= 1;
    ++answer;
  }

  // output
  cout << answer << endl;
}
