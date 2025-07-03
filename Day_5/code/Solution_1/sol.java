import java.util.*;

public class sol {

    static class FenwickTree {
        int[] bit;
        int size;

        FenwickTree(int n) {
            size = n;
            bit = new int[n + 2];
        }

        void update(int index, int delta) {
            while (index <= size) {
                bit[index] += delta;
                index += index & -index;
            }
        }

        int query(int index) {
            int sum = 0;
            while (index > 0) {
                sum += bit[index];
                index -= index & -index;
            }
            return sum;
        }
    }

    public static int countSpecialPairs(int[] a) {
        int n = a.length;

        int[] prefix = new int[n];
        int[] suffix = new int[n];
        Map<Integer, Integer> freq = new HashMap<>();

        // Compute prefix frequencies
        for (int i = 0; i < n; i++) {
            freq.put(a[i], freq.getOrDefault(a[i], 0) + 1);
            prefix[i] = freq.get(a[i]);
        }

        // Compute suffix frequencies
        freq.clear();
        for (int i = n - 1; i >= 0; i--) {
            freq.put(a[i], freq.getOrDefault(a[i], 0) + 1);
            suffix[i] = freq.get(a[i]);
        }

        FenwickTree bit = new FenwickTree(n);
        for (int val : suffix)
            bit.update(val, 1);

        int ans = 0;
        for (int i = 0; i < n; i++) {
            bit.update(suffix[i], -1);
            ans += bit.query(prefix[i] - 1);
        }

        return ans;
    }

    public static void main(String[] args) {
        int[] arr1 = {1, 2, 1, 1, 2, 2, 1};
        System.out.println(countSpecialPairs(arr1));  // Output: 8
    }
}

