# TreeNode class
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)


# Tree class
class Tree:
    def __init__(self, root):
        self.root = root

    def print_tree(self, node=None, level=0):
        if node is None:
            node = self.root
        print(" " * (level * 2) + str(node.data))
        for child in node.children:
            self.print_tree(child, level + 1)

    def find(self, data, node=None):
        if node is None:
            node = self.root
        if node.data == data:
            return node
        for child in node.children:
            result = self.find(data, child)
            if result:
                return result
        return None

    def get_height(self, node=None):
        if node is None:
            node = self.root
        if not node.children:
            return 1
        return 1 + max(self.get_height(child) for child in node.children)

    def count_nodes(self, node=None):
        if node is None:
            node = self.root
        count = 1
        for child in node.children:
            count += self.count_nodes(child)
        return count

    def print_list(self, node=None):
        if node is None:
            node = self.root
        print(node.data, end=" ")
        for child in node.children:
            self.print_list(child)



if __name__ == "__main__":
    # Create tree
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Dell"))

    phone = TreeNode("Phone")
    phone.add_child(TreeNode("iPhone"))
    phone.add_child(TreeNode("Samsung"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Sony"))
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(phone)
    root.add_child(tv)

    tree = Tree(root)

    # Function Tests
    print("Tree structure:")
    tree.print_tree()
    
    print("\n\nSearch for 'iPhone':")
    found = tree.find("iPhone")
    print("Found:", found.data if found else "Not found")

    print("\nTree height:", tree.get_height())
    print("Total nodes:", tree.count_nodes())

    print("Tree values in sequence:")
    tree.print_list()
