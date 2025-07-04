import java.util.*;

public class sol {
    static class FenwickTree {
        int[] tree;
        int n;

        FenwickTree(int size) {
            this.n = size;
            tree = new int[n + 1];
        }

        void update(int index, int delta) {
            while (index <= n) {
                tree[index] += delta;
                index += index & -index;
            }
        }

        int query(int index) {
            int result = 0;
            while (index > 0) {
                result += tree[index];
                index -= index & -index;
            }
            return result;
        }
    }

    public static void main(String[] args) {
        int[] a = {3, 3, 1, 6, 1};
        int n = a.length;

        // Coordinate compression
        TreeSet<Integer> sortedSet = new TreeSet<>();
        for (int val : a) sortedSet.add(val);

        List<Integer> sortedList = new ArrayList<>(sortedSet);
        Map<Integer, Integer> compressMap = new HashMap<>();
        for (int i = 0; i < sortedList.size(); i++) {
            compressMap.put(sortedList.get(i), i + 1);
        }

        FenwickTree fenwick = new FenwickTree(sortedList.size());
        for (int i = 1; i <= sortedList.size(); i++) {
            fenwick.update(i, 1);
        }

        Map<Integer, Integer> rankMap = new HashMap<>();
        for (int val : sortedList) {
            int index = compressMap.get(val);
            rankMap.put(val, fenwick.query(index - 1));
        }

        for (int val : a) {
            System.out.println(rankMap.get(val));
        }
    }
}
