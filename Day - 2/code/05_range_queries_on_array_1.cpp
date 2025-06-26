#include <iostream>
#include <vector>
using namespace std;

const int MOD = 1e9 + 7;

int process_queries(int n, vector<int>& A, vector<vector<int>>& queries) {
    long long total_sum = 0;

    for (auto& query : queries) {
        int type = query[0];
        int l = query[1];
        int r = query[2];

        if (type == 1) {
            // Type 1: Update A[i] from index l to r
            int base = A[l];
            for (int i = l; i <= r; ++i) {
                A[i] = (i - l + 1) * base;
            }
        } else if (type == 2) {
            // Type 2: Sum A[l] to A[r]
            long long sum = 0;
            for (int i = l; i <= r; ++i) {
                sum += A[i];
            }
            total_sum = (total_sum + sum) % MOD;
        }
    }

    return total_sum;
}

int main() {
    int n = 7;
    vector<int> A = {1, 4, 5, 1, 6, 7, 8};
    vector<vector<int>> queries = {
        {1, 1, 6},
        {1, 1, 5},
        {2, 5, 5},
        {2, 3, 4},
        {2, 3, 3}
    };

    cout << process_queries(n, A, queries) << endl;  // Output: 60
    return 0;
}
