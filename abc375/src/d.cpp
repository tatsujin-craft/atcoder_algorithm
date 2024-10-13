#include <iostream>
#include <string>

using namespace std;

int count_palindromic_triplets(const string &S) {
  int n = S.size();
  int count = 0;
  for (int i = 0; i < n - 2; i++) {
    for (int j = i + 1; j < n - 1; j++) {
      for (int k = j + 1; k < n; k++) {
        if (S[i] == S[k]) {
          count++;
        }
      }
    }
  }
  return count;
}

int main() {
  string S;
  cin >> S;
  cout << count_palindromic_triplets(S) << endl;
  return 0;
}
