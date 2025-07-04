import java.util.ArrayList;
import java.util.List;

class TreeNode {
    String data;
    List<TreeNode> children;

    TreeNode(String data) {
        this.data = data;
        this.children = new ArrayList<>();
    }

    void addChild(TreeNode child) {
        children.add(child);
    }
}

class Tree {
    TreeNode root;

    Tree(TreeNode root) {
        this.root = root;
    }

    void printTree(TreeNode node, int level) {
        if (node == null) return;
        System.out.println(" ".repeat(level * 2) + node.data);
        for (TreeNode child : node.children) {
            printTree(child, level + 1);
        }
    }

    void printTree() {
        printTree(root, 0);
    }

    TreeNode find(String data, TreeNode node) {
        if (node == null) return null;
        if (node.data.equals(data)) return node;
        for (TreeNode child : node.children) {
            TreeNode result = find(data, child);
            if (result != null) return result;
        }
        return null;
    }

    TreeNode find(String data) {
        return find(data, root);
    }

    int getHeight(TreeNode node) {
        if (node.children.isEmpty()) return 1;
        int maxHeight = 0;
        for (TreeNode child : node.children) {
            maxHeight = Math.max(maxHeight, getHeight(child));
        }
        return 1 + maxHeight;
    }

    int getHeight() {
        return getHeight(root);
    }

    int countNodes(TreeNode node) {
        int count = 1;
        for (TreeNode child : node.children) {
            count += countNodes(child);
        }
        return count;
    }

    int countNodes() {
        return countNodes(root);
    }

    void printList(TreeNode node) {
        System.out.print(node.data + " ");
        for (TreeNode child : node.children) {
            printList(child);
        }
    }

    void printList() {
        printList(root);
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode("Electronics");

        TreeNode laptop = new TreeNode("Laptop");
        laptop.addChild(new TreeNode("Mac"));
        laptop.addChild(new TreeNode("Dell"));

        TreeNode phone = new TreeNode("Phone");
        phone.addChild(new TreeNode("iPhone"));
        phone.addChild(new TreeNode("Samsung"));

        TreeNode tv = new TreeNode("TV");
        tv.addChild(new TreeNode("Sony"));
        tv.addChild(new TreeNode("LG"));

        root.addChild(laptop);
        root.addChild(phone);
        root.addChild(tv);

        Tree tree = new Tree(root);

        System.out.println("Tree structure:");
        tree.printTree();

        System.out.println("\nSearch for 'iPhone':");
        TreeNode found = tree.find("iPhone");
        System.out.println("Found: " + (found != null ? found.data : "Not found"));

        System.out.println("\nTree height: " + tree.getHeight());
        System.out.println("Total nodes: " + tree.countNodes());

        System.out.print("Tree values in sequence: ");
        tree.printList();
    }
}
