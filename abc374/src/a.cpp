/**
 * @file    a.cpp
 * @brief   This program checks if a string ends with "san".
 * @author  tatsujin
 * @date    2024-10-06
 */

#include <bits/stdc++.h>
using namespace std;

int main() {
  string s;
  cin >> s;

  if (s.substr(s.size() - 3) == "san")
    cout << "Yes" << endl;
  else
    cout << "No" << endl;

  return 0;
}
