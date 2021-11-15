# the code is lifted and translated from https://github.com/gkcs/Competitive-Programming/blob/master/src/main/java/main/java/videos/LCA.java
class LeastCommonAncestor:
    def build_graph():
        vert_count = int(input().strip())
        edge_count = vert_count - 1
        from_edges = [None] * edge_count
        to_edges = [None] * edge_count
 
