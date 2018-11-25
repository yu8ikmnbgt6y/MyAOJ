import sys
import io

input_txt = """
11
0 1 2 3 9 10 4 5 6 7 8
2 1 9 3 10 0 6 5 7 4 8
"""
#2 9 10 3 1 6 7 5 8 4 0



sys.stdin = io.StringIO(input_txt)
tmp = input()


# copy the below part and paste to the submission form.
# ---------function------------
def reconstruct(preorder, inorder, postorder):
    if len(preorder) == 0:
        return
    node_no = preorder[0]
    node_div = inorder.index(node_no)

    reconstruct(preorder[1:node_div+1], inorder[:node_div], postorder)
    reconstruct(preorder[node_div+1:], inorder[node_div+1:], postorder)

    postorder.append(node_no)
    return

def main():
    input()
    preorder = [int(x) for x in input().split()]
    inorder = [int(x) for x in input().split()]

    postorder = []
    reconstruct(preorder, inorder, postorder)
    print(" ".join(map(str, postorder)))

main()
# -----------------------------
sys.stdin = sys.__stdin__
