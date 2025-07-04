import java.util.*;

public class MatrixQueryProcessor {
    static final int MOD = 1_000_000_007;

    public static int processQueries(int n, int[] A, int[][] queries) {
        long totalSum = 0;

        for (int[] query : queries) {
            int type = query[0];
            int l = query[1];
            int r = query[2];

            if (type == 1) {
                int base = A[l];
                for (int i = l; i <= r; i++) {
                    A[i] = (i - l + 1) * base;
                }
            } else if (type == 2) {
                long sum = 0;
                for (int i = l; i <= r; i++) {
                    sum += A[i];
                }
                totalSum = (totalSum + sum) % MOD;
            }
        }

        return (int) totalSum;
    }

    public static void main(String[] args) {
        int n = 7;
        int[] A = {1, 4, 5, 1, 6, 7, 8};
        int[][] queries = {
            {1, 1, 6},
            {1, 1, 5},
            {2, 5, 5},
            {2, 3, 4},
            {2, 3, 3}
        };

        System.out.println(processQueries(n, A, queries));  // Output: 60
    }
}
