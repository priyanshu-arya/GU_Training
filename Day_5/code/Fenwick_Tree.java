package Day_5.code;

class Fenwick_Tree {
    int[] tree;
    int n;

    public Fenwick_Tree(int size) {
        n = size;
        tree = new int[n + 1];
    }

    public void update(int index, int delta) {
        while (index <= n) {
            tree[index] += delta;
            index += index & -index;
        }
    }

    public int prefixSum(int index) {
        int result = 0;
        while (index > 0) {
            result += tree[index];
            index -= index & -index;
        }
        return result;
    }

    public int rangeSum(int left, int right) {
        return prefixSum(right) - prefixSum(left - 1);
    }

    public static void main(String[] args) {
        Fenwick_Tree ft = new Fenwick_Tree(10);
        ft.update(3, 5);
        ft.update(5, 2);
        System.out.println(ft.rangeSum(3, 5)); // Output: 7
    }
}

