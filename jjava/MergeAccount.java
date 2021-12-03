import java.util.*;

class DSU {
    int representative[];
    int size[];

    DSU(int sz) {
        representative = new int[sz];
        size = new int[sz];

        for (int i = 0; i < sz; ++i) {
            // Initially each group is its own representative
            representative[i] = i;
            // Intialize the size of all groups to 1
            size[i] = 1;
        }
    }

    // Finds the representative of group x
    public int findRepresentative(int x) {
        if (x == representative[x]) {
            return x;
        }

        // This is path compression
        return representative[x] = findRepresentative(representative[x]);
    }

    // Unite the group that contains "a" with the group that contains "b"
    public void unionBySize(int a, int b) {
        int representativeA = findRepresentative(a);
        int representativeB = findRepresentative(b);

        // If nodes a and b already belong to the same group, do nothing.
        if (representativeA == representativeB) {
            return;
        }

        // Union by size: point the representative of the smaller
        // group to the representative of the larger group.
        if (size[representativeA] >= size[representativeB]) {
            size[representativeA] += size[representativeB];
            representative[representativeB] = representativeA;
        } else {
            size[representativeB] += size[representativeA];
            representative[representativeA] = representativeB;
        }
    }
}

class MergeAccount {
    public static void main(String[] args) {
//        accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],
//        ["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],
//        ["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],
//        ["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],
//        ["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]

        MergeAccount sol = new MergeAccount();
        List<List<String>> ll = new ArrayList<>();
//        String[] s1 = {"Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe1@m.co"};
        String[] s1 = {"John", "johnsmith@mail.com", "john_newyork@mail.com"};
        List<String> l1 = Arrays.asList(s1);
//        String[] s2 = {"Kevin", "Kevin3@m.co", "Kevin5@m.co", "Kevin0@m.co"};
        String[] s2 = {"John", "johnsmith@mail.com", "john00@mail.com"};
        List<String> l2 = Arrays.asList(s2);
        String[] s3 = {"John", "johnnybravo@mail.com"};
//        String[] s3 = {"Ethan", "Ethan5@m.co", "Ethan4@m.co", "Ethan0@m.co"};
        List<String> l3 = Arrays.asList(s3);
//        String[] s4 = {"Hanzo", "Hanzo3@m.co", "Hanzo1@m.co", "Hanzo0@m.co"};
//        List<String> l4 = Arrays.asList(s4);
//        String[] s5 = {"Fern", "Fern5@m.co", "Fern1@m.co", "Fern0@m.co"};
//        List<String> l5 = Arrays.asList(s5);
        ll.add(l1);
        ll.add(l2);
        ll.add(l3);
//        ll.add(l4);
//        ll.add(l5);

        System.out.println(sol.accountsMerge(ll));
    }

    public List<List<String>> accountsMerge(List<List<String>> accountList) {
        int accountListSize = accountList.size();
        DSU dsu = new DSU(accountListSize);

        // Maps email to their component index
        Map<String, Integer> emailGroup = new HashMap<>();

        for (int i = 0; i < accountListSize; i++) {
            int accountSize = accountList.get(i).size();

            for (int j = 1; j < accountSize; j++) {
                String email = accountList.get(i).get(j);
                String accountName = accountList.get(i).get(0);

                // If this is the first time seeing this email then
                // assign component group as the account index
                if (!emailGroup.containsKey(email)) {
                    emailGroup.put(email, i);
                } else {
                    // If we have seen this email before then union this
                    // group with the previous group of the email
                    dsu.unionBySize(i, emailGroup.get(email));
                }
            }
        }

        // Store emails corresponding to the component's representative
        Map<Integer, List<String>> components = new HashMap<Integer, List<String>>();
        for (String email : emailGroup.keySet()) {
            int group = emailGroup.get(email);
            int groupRep = dsu.findRepresentative(group);

            if (!components.containsKey(groupRep)) {
                components.put(groupRep, new ArrayList<String>());
            }

            components.get(groupRep).add(email);
        }

        // Sort the components and add the account name
        List<List<String>> mergedAccounts = new ArrayList<>();
        for (int group : components.keySet()) {
            List<String> component = components.get(group);
            Collections.sort(component);
            component.add(0, accountList.get(group).get(0));
            mergedAccounts.add(component);
        }

        return mergedAccounts;
    }
}