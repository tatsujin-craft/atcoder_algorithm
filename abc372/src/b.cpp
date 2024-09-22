#include <iostream>
#include <vector>
using namespace std;

int main() {
  int M;
  cin >> M;
  vector<int> A;

  for (int k = 0; k <= 10; k++) {
    for (int i = 0; i < (M % 3); i++) {
      A.push_back(k);
    }
    M /= 3;
  }

  cout << A.size() << endl;
  for (int i = 0; i < A.size(); i++) {
    cout << A[i] << " \n"[i == A.size() - 1];
  }
  return 0;
}
