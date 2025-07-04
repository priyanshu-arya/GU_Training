import java.util.*;

public class QueryProcessor {

    static final int MOD = (int) 1e9 + 7;

    public static int processQueries(int n, int[] A, List<int[]> queries) {
        long totalSum = 0;

        for (int[] query : queries) {
            int type = query[0];
            int l = query[1];
            int r = query[2];

            // Type 1: Update A[i] from index l to r
            // Type 2: Sum from A[l] to A[r] and add to totalSum
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

        List<int[]> queries = new ArrayList<>();
        queries.add(new int[]{1, 1, 6});
        queries.add(new int[]{1, 1, 5});
        queries.add(new int[]{2, 5, 5});
        queries.add(new int[]{2, 3, 4});
        queries.add(new int[]{2, 3, 3});

        int result = processQueries(n, A, queries);
        System.out.println(result); // Output: 60
    }
}
