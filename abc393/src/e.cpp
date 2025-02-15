#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> get_max_gcds(int k, const vector<int>& a_list) {
    if (k == 1)
        return a_list;

    int max_a = *max_element(a_list.begin(), a_list.end());
    vector<int> freq(max_a + 1, 0);
    for (int a : a_list)
        freq[a]++;

    vector<int> count_divisible(max_a + 1, 0);
    int upper_limit = max_a + 1;
    for (int divisor = 1; divisor < upper_limit; divisor++) {
        int total = 0;
        for (int multiple = divisor; multiple < upper_limit; multiple += divisor)
            total += freq[multiple];
        count_divisible[divisor] = total;
    }

    vector<int> max_possible_gcd(max_a + 1, 0);
    for (int divisor = max_a; divisor > 0; divisor--) {
        if (count_divisible[divisor] >= k) {
            for (int multiple = divisor; multiple < upper_limit; multiple += divisor) {
                if (max_possible_gcd[multiple] == 0)
                    max_possible_gcd[multiple] = divisor;
            }
        }
    }

    vector<int> result;
    result.reserve(a_list.size());
    for (int a : a_list)
        result.push_back(max_possible_gcd[a]);
    return result;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    cin >> n >> k;
    vector<int> a_list(n);
    for (int i = 0; i < n; i++)
        cin >> a_list[i];

    vector<int> results = get_max_gcds(k, a_list);
    for (int r : results)
        cout << r << "\n";

    return 0;
}
