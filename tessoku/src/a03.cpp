#include <iostream>
#include <vector>
using namespace std;

void find_target_pair() {
  int n, k;
  cin >> n >> k;

  vector<int> p_list(n);
  vector<int> q_list(n);

  for (int i = 0; i < n; ++i) {
    cin >> p_list[i];
  }

  for (int i = 0; i < n; ++i) {
    cin >> q_list[i];
  }

  bool is_exist = false;
  int p_value = 0, q_value = 0;

  for (int p : p_list) {
    for (int q : q_list) {
      if (p + q == k) {
        is_exist = true;
        p_value = p;
        q_value = q;
        break;
      }
    }
    if (is_exist) {
      break;
    }
  }

  if (is_exist) {
    cout << "Yes" << endl;
    cout << "Found pair: p=" << p_value << ", q=" << q_value << ", k=" << k
         << endl;
  } else {
    cout << "No" << endl;
  }
}

int main() {
  find_target_pair();
  return 0;
}
