#include <bits/stdc++.h>
using namespace std;

class DualHeap {
    priority_queue<int> small;
    priority_queue<int, vector<int>, greater<>> large;
    unordered_map<int, int> delayed;
    int k, smallSize = 0, largeSize = 0;

    void prune(priority_queue<int>& heap) {
        while (!heap.empty()) {
            int num = heap.top();
            if (delayed[num]) {
                delayed[num]--;
                heap.pop();
            } else break;
        }
    }

    void prune(priority_queue<int, vector<int>, greater<>>& heap) {
        while (!heap.empty()) {
            int num = heap.top();
            if (delayed[num]) {
                delayed[num]--;
                heap.pop();
            } else break;
        }
    }

    void balance() {
        if (smallSize > largeSize + 1) {
            int val = small.top(); small.pop();
            large.push(val);
            smallSize--; largeSize++;
            prune(small);
        } else if (smallSize < largeSize) {
            int val = large.top(); large.pop();
            small.push(val);
            largeSize--; smallSize++;
            prune(large);
        }
    }

public:
    DualHeap(int k): k(k) {}

    void insert(int num) {
        if (small.empty() || num <= small.top()) {
            small.push(num);
            smallSize++;
        } else {
            large.push(num);
            largeSize++;
        }
        balance();
    }

    void erase(int num) {
        delayed[num]++;
        if (!small.empty() && num <= small.top()) smallSize--;
        else largeSize--;
        balance();
    }

    double getMedian() {
        return k % 2 ? small.top() : ((long long)small.top() + large.top()) / 2.0;
    }
};

vector<double> medianSlidingWindow(vector<int>& nums, int k) {
    DualHeap dh(k);
    vector<double> res;
    for (int i = 0; i < k; ++i) dh.insert(nums[i]);
    res.push_back(dh.getMedian());

    for (int i = k; i < nums.size(); ++i) {
        dh.insert(nums[i]);
        dh.erase(nums[i - k]);
        res.push_back(dh.getMedian());
    }
    return res;
}
