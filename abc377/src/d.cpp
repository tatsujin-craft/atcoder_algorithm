#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int count_by_interval_scheduling(int M, vector<pair<int, int>> &intervals) {
  sort(intervals.begin(), intervals.end()); // 区間のソート
  vector<int> end_points;

  for (const auto &interval : intervals) {
    end_points.push_back(interval.second); // 終端点のみ抽出
  }
  sort(end_points.begin(), end_points.end());

  int count = 0;

  for (int l = 1; l <= M; ++l) {
    int r_idx = lower_bound(end_points.begin(), end_points.end(), l) -
                end_points.begin(); // 二分探索でインデックスを取得
    int temp_count = 0;

    for (int r = l; r <= M; ++r) {
      bool include_all = false;
      for (const auto &interval : intervals) {
        int L = interval.first, R = interval.second;
        if (L >= l && R <= r) {
          include_all = true;
          break;
        }
      }
      if (!include_all) {
        temp_count++;
      }
    }

    count += temp_count;
  }

  return count;
}

int main() {
  int N, M;
  cin >> N >> M;
  vector<pair<int, int>> intervals(N);

  for (int i = 0; i < N; ++i) {
    int L, R;
    cin >> L >> R;
    intervals[i] = {L, R};
  }

  int interval_count = count_by_interval_scheduling(M, intervals);
  cout << interval_count << endl;

  return 0;
}
