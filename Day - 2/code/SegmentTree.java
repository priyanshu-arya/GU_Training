public class SegmentTree {

    private static class Node {
        int start, end, data;
        Node left, right;

        Node(int start, int end) {
            this.start = start;
            this.end = end;
        }
    }

    private Node root;

    public SegmentTree(int[] arr) {
        this.root = construct(arr, 0, arr.length - 1);
    }

    private Node construct(int[] arr, int start, int end) {
        if (start == end) {
            Node leaf = new Node(start, end);
            leaf.data = arr[start];
            return leaf;
        }

        Node node = new Node(start, end);
        int mid = (start + end) / 2;
        node.left = construct(arr, start, mid);
        node.right = construct(arr, mid + 1, end);
        node.data = node.left.data + node.right.data;
        return node;
    }

    // public void display() {
    //     display(this.root);
    // }

    // private void display(Node node) {
    //     if (node == null) return;

    //     String left = node.left != null ? "[" + node.left.start + "-" + node.left.end + "] => " + node.left.data : "No left child";
    //     String right = node.right != null ? "[" + node.right.start + "-" + node.right.end + "] => " + node.right.data : "No right child";
    //     String curr = "[" + node.start + "-" + node.end + "] => " + node.data;

    //     System.out.println(left + " <= " + curr + " => " + right + "\n");

    //     display(node.left);
    //     display(node.right);
    // }

    public int query(int qsi, int qei) {
        return query(this.root, qsi, qei);
    }

    private int query(Node node, int qsi, int qei) {
        if (node.start >= qsi && node.end <= qei) {
            return node.data;
        } else if (node.end < qsi || node.start > qei) {
            return 0;
        }
        return query(node.left, qsi, qei) + query(node.right, qsi, qei);
    }

    public void update(int index, int value) {
        this.root.data = update(this.root, index, value);
    }

    public void updateRange(int start, int end, int value) {
        for (int i = start; i <= end; i++) {
            this.root.data = update(this.root, i, value);
        }
    }

    private int update(Node node, int index, int value) {
        if (index < node.start || index > node.end) return node.data;

        if (node.start == node.end) {
            node.data = value;
            return node.data;
        }

        int left = update(node.left, index, value);
        int right = update(node.right, index, value);
        node.data = left + right;
        return node.data;
    }

    public static void main(String[] args) {
        int[] arr = {1, 3, 5, 7, 9, 11};
        SegmentTree st = new SegmentTree(arr);

        // st.display();

        System.out.println("Query(1, 3): " + st.query(1, 3)); // 15
        st.update(1, 10);
        System.out.println("Query(1, 3) after update: " + st.query(1, 3)); // 22

        st.updateRange(3, 5, 20);
        System.out.println("Query(1, 3) after range update: " + st.query(1, 3)); // 22

        // st.display();
    }
}
