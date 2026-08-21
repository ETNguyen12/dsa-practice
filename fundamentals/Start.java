// ============================================================================
// Start.java - the Java drill runner (tests + timer). Don't edit this.
// Fill in Drill.java, then:  javac Drill.java Start.java && java Start
// The timer starts on your first `java Start` and persists in .drill.start
// across re-runs, resetting on a full CORE clear.
// ============================================================================
import java.util.*;
import java.io.*;
import java.nio.file.*;
import java.util.function.BooleanSupplier;

public class Start {
    // ---- builders ----------------------------------------------------------
    static final Integer NIL = null;

    static Drill.ListNode buildL(int... vals) {
        Drill.ListNode dummy = new Drill.ListNode(), cur = dummy;
        for (int v : vals) { cur.next = new Drill.ListNode(v); cur = cur.next; }
        return dummy.next;
    }
    static List<Integer> toL(Drill.ListNode h) {
        List<Integer> o = new ArrayList<>();
        while (h != null) { o.add(h.val); h = h.next; }
        return o;
    }
    static Drill.TreeNode buildT(Integer... vals) {
        if (vals.length == 0 || vals[0] == null) return null;
        Drill.TreeNode root = new Drill.TreeNode(vals[0]);
        Deque<Drill.TreeNode> q = new ArrayDeque<>(); q.offer(root);
        int i = 1;
        while (!q.isEmpty() && i < vals.length) {
            Drill.TreeNode n = q.poll();
            if (i < vals.length) { if (vals[i] != null) { n.left = new Drill.TreeNode(vals[i]); q.offer(n.left); } i++; }
            if (i < vals.length) { if (vals[i] != null) { n.right = new Drill.TreeNode(vals[i]); q.offer(n.right); } i++; }
        }
        return root;
    }
    static List<Integer> inorder(Drill.TreeNode r) {
        List<Integer> o = new ArrayList<>();
        inorderGo(r, o);
        return o;
    }
    static void inorderGo(Drill.TreeNode n, List<Integer> o) {
        if (n == null) return;
        inorderGo(n.left, o); o.add(n.val); inorderGo(n.right, o);
    }
    static Map<Integer, List<Integer>> G() {
        Map<Integer, List<Integer>> g = new HashMap<>();
        g.put(0, Arrays.asList(1, 2)); g.put(1, Arrays.asList(0, 3));
        g.put(2, Arrays.asList(0, 3)); g.put(3, Arrays.asList(1, 2));
        return g;
    }
    // normalize a list of int-lists (sort within, sort across) for order-free compare
    static List<List<Integer>> normI(List<List<Integer>> xss) {
        List<List<Integer>> out = new ArrayList<>();
        for (List<Integer> x : xss) { List<Integer> c = new ArrayList<>(x); Collections.sort(c); out.add(c); }
        out.sort(Comparator.comparing(Object::toString));
        return out;
    }
    static List<List<String>> normS(List<List<String>> gs) {
        List<List<String>> out = new ArrayList<>();
        for (List<String> g : gs) { List<String> c = new ArrayList<>(g); Collections.sort(c); out.add(c); }
        out.sort(Comparator.comparing(Object::toString));
        return out;
    }
    static List<List<Integer>> LL(int[][] rows) {
        List<List<Integer>> o = new ArrayList<>();
        for (int[] r : rows) { List<Integer> l = new ArrayList<>(); for (int v : r) l.add(v); o.add(l); }
        return o;
    }

    // ---- a test case -------------------------------------------------------
    static class Case { String name; boolean core; BooleanSupplier run; Case(String n, boolean c, BooleanSupplier r) { name = n; core = c; run = r; } }

    static List<Case> cases() {
        List<Case> c = new ArrayList<>();
        c.add(new Case("reverseList", true, () -> toL(Drill.reverseList(buildL(1,2,3,4,5))).equals(Arrays.asList(5,4,3,2,1)) && toL(Drill.reverseList(buildL())).equals(Collections.emptyList()) && toL(Drill.reverseList(buildL(1))).equals(Arrays.asList(1))));
        c.add(new Case("deleteMiddleNode", true, () -> toL(Drill.deleteMiddleNode(buildL(1,3,4,7,1,2,6))).equals(Arrays.asList(1,3,4,1,2,6)) && toL(Drill.deleteMiddleNode(buildL(1,2,3,4))).equals(Arrays.asList(1,2,4)) && toL(Drill.deleteMiddleNode(buildL(2,1))).equals(Arrays.asList(2)) && toL(Drill.deleteMiddleNode(buildL(1))).equals(Collections.emptyList())));
        c.add(new Case("oddEvenList", true, () -> toL(Drill.oddEvenList(buildL(1,2,3,4,5))).equals(Arrays.asList(1,3,5,2,4)) && toL(Drill.oddEvenList(buildL(2,1,3,5,6,4,7))).equals(Arrays.asList(2,3,6,7,1,5,4)) && toL(Drill.oddEvenList(buildL())).equals(Collections.emptyList()) && toL(Drill.oddEvenList(buildL(1))).equals(Arrays.asList(1))));
        c.add(new Case("dfsIterative", true, () -> Drill.dfsIterative(G(), 0).equals(Arrays.asList(0,2,3,1))));
        c.add(new Case("bfs", true, () -> Drill.bfs(G(), 0).equals(Arrays.asList(0,1,2,3))));
        c.add(new Case("dfsRecursive", true, () -> Drill.dfsRecursive(G(), 0).equals(Arrays.asList(0,1,3,2))));
        c.add(new Case("topK", true, () -> Drill.topK(new int[]{3,1,8,2,9,4}, 3).equals(Arrays.asList(9,8,4)) && Drill.topK(new int[]{5}, 1).equals(Arrays.asList(5))));
        c.add(new Case("binarySearch", true, () -> { int[] a={1,3,5,7,9}; return Drill.binarySearch(a,7)==3 && Drill.binarySearch(a,1)==0 && Drill.binarySearch(a,9)==4 && Drill.binarySearch(a,4)==-1 && Drill.binarySearch(new int[]{},1)==-1; }));
        c.add(new Case("lowerBound", true, () -> { int[] a={1,3,3,5}; return Drill.lowerBound(a,3)==1 && Drill.lowerBound(a,4)==3 && Drill.lowerBound(a,6)==4 && Drill.lowerBound(a,0)==0; }));
        c.add(new Case("maxWindowSum", true, () -> Drill.maxWindowSum(new int[]{2,1,5,1,3,2},3)==9 && Drill.maxWindowSum(new int[]{1,2,3},3)==6 && Drill.maxWindowSum(new int[]{4},1)==4));
        c.add(new Case("longestUniqueSubstring", true, () -> Drill.longestUniqueSubstring("abcabcbb")==3 && Drill.longestUniqueSubstring("bbbbb")==1 && Drill.longestUniqueSubstring("pwwkew")==3 && Drill.longestUniqueSubstring("")==0));
        c.add(new Case("maxDepth", true, () -> Drill.maxDepth(buildT(3,9,20,NIL,NIL,15,7))==3 && Drill.maxDepth(buildT())==0 && Drill.maxDepth(buildT(1))==1));
        c.add(new Case("levelOrder", true, () -> Drill.levelOrder(buildT(3,9,20,NIL,NIL,15,7)).equals(LL(new int[][]{{3},{9,20},{15,7}})) && Drill.levelOrder(buildT()).equals(Collections.emptyList()) && Drill.levelOrder(buildT(1)).equals(LL(new int[][]{{1}}))));
        c.add(new Case("isValidBst", true, () -> Drill.isValidBst(buildT(2,1,3)) && !Drill.isValidBst(buildT(5,1,4,NIL,NIL,3,6)) && !Drill.isValidBst(buildT(5,4,6,NIL,NIL,3,7)) && Drill.isValidBst(buildT(1))));
        c.add(new Case("searchBst", true, () -> { Drill.TreeNode r = Drill.searchBst(buildT(4,2,7,1,3), 2); return r != null && r.val == 2 && inorder(r).equals(Arrays.asList(1,2,3)) && Drill.searchBst(buildT(4,2,7,1,3), 5) == null; }));
        c.add(new Case("groupAnagrams", true, () -> normS(Drill.groupAnagrams(new String[]{"eat","tea","tan","ate","nat","bat"})).equals(normS(Arrays.asList(Arrays.asList("eat","tea","ate"), Arrays.asList("tan","nat"), Arrays.asList("bat"))))));
        c.add(new Case("numIslands", true, () -> Drill.numIslands(new int[][]{{1,1,0,0,0},{1,1,0,0,0},{0,0,1,0,0},{0,0,0,1,1}})==3 && Drill.numIslands(new int[][]{{1,1,1,1,0},{1,1,0,1,0},{1,1,0,0,0},{0,0,0,0,0}})==1 && Drill.numIslands(new int[][]{{0,0},{0,0}})==0));
        c.add(new Case("threeSum", true, () -> normI(Drill.threeSum(new int[]{-1,0,1,2,-1,-4})).equals(normI(LL(new int[][]{{-1,-1,2},{-1,0,1}}))) && normI(Drill.threeSum(new int[]{0,0,0})).equals(normI(LL(new int[][]{{0,0,0}}))) && Drill.threeSum(new int[]{0,1,1}).equals(Collections.emptyList())));
        c.add(new Case("dailyTemperatures", true, () -> Arrays.equals(Drill.dailyTemperatures(new int[]{73,74,75,71,69,72,76,73}), new int[]{1,1,4,2,1,1,0,0}) && Arrays.equals(Drill.dailyTemperatures(new int[]{30,40,50,60}), new int[]{1,1,1,0}) && Arrays.equals(Drill.dailyTemperatures(new int[]{30,60,90}), new int[]{1,1,0})));
        c.add(new Case("mergeIntervals", true, () -> Arrays.deepEquals(Drill.mergeIntervals(new int[][]{{1,3},{2,6},{8,10},{15,18}}), new int[][]{{1,6},{8,10},{15,18}}) && Arrays.deepEquals(Drill.mergeIntervals(new int[][]{{1,4},{4,5}}), new int[][]{{1,5}}) && Arrays.deepEquals(Drill.mergeIntervals(new int[][]{{1,4},{0,2},{3,5}}), new int[][]{{0,5}})));
        c.add(new Case("deleteBstNode", true, () -> inorder(Drill.deleteBstNode(buildT(5,3,6,2,4,NIL,7), 3)).equals(Arrays.asList(2,4,5,6,7)) && inorder(Drill.deleteBstNode(buildT(5,3,6,2,4,NIL,7), 7)).equals(Arrays.asList(2,3,4,5,6)) && inorder(Drill.deleteBstNode(buildT(5,3,6,2,4,NIL,7), 5)).equals(Arrays.asList(2,3,4,6,7)) && inorder(Drill.deleteBstNode(buildT(1), 1)).equals(Collections.emptyList())));
        c.add(new Case("subsets", true, () -> normI(Drill.subsets(new int[]{1,2,3})).equals(normI(LL(new int[][]{{},{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}}))) && normI(Drill.subsets(new int[]{})).equals(normI(LL(new int[][]{{}}))) && normI(Drill.subsets(new int[]{0})).equals(normI(LL(new int[][]{{},{0}})))));
        c.add(new Case("minEatingSpeed", true, () -> Drill.minEatingSpeed(new int[]{3,6,7,11},8)==4 && Drill.minEatingSpeed(new int[]{30,11,23,4,20},5)==30 && Drill.minEatingSpeed(new int[]{30,11,23,4,20},6)==23));
        c.add(new Case("subarraySum", true, () -> Drill.subarraySum(new int[]{1,1,1},2)==2 && Drill.subarraySum(new int[]{1,2,3},3)==2 && Drill.subarraySum(new int[]{1,-1,0},0)==3));

        c.add(new Case("coinChange", false, () -> Drill.coinChange(new int[]{1,2,5},11)==3 && Drill.coinChange(new int[]{2},3)==-1 && Drill.coinChange(new int[]{1},0)==0 && Drill.coinChange(new int[]{1,5,10,25},30)==2));
        c.add(new Case("courseSchedule", false, () -> Drill.courseSchedule(2,new int[][]{{1,0}}) && !Drill.courseSchedule(2,new int[][]{{1,0},{0,1}}) && Drill.courseSchedule(4,new int[][]{{1,0},{2,1},{3,2}})));
        c.add(new Case("uniquePaths", false, () -> Drill.uniquePaths(3,7)==28 && Drill.uniquePaths(3,2)==3 && Drill.uniquePaths(1,1)==1));
        c.add(new Case("diameterOfBinaryTree", false, () -> Drill.diameterOfBinaryTree(buildT(1,2,3,4,5))==3 && Drill.diameterOfBinaryTree(buildT(1))==0 && Drill.diameterOfBinaryTree(buildT(1,2))==1));
        return c;
    }

    static String fmt(double secs) { int m = (int) secs / 60, s = (int) secs % 60; return String.format("%dm %02ds", m, s); }

    public static void main(String[] args) throws IOException {
        Path mark = Paths.get(".drill.start");
        List<Case> cs = cases();

        double start; boolean fresh;
        if (Files.exists(mark)) { start = Double.parseDouble(new String(Files.readAllBytes(mark)).trim()); fresh = false; }
        else { start = System.currentTimeMillis() / 1000.0; Files.write(mark, String.valueOf(start).getBytes()); fresh = true; }
        double elapsed = System.currentTimeMillis() / 1000.0 - start;

        System.out.println("\n" + "=".repeat(40));
        int corePass = 0, coreTotal = 0;
        for (Case c : cs) {
            if (!c.core) continue;
            coreTotal++;
            boolean ok;
            try { ok = c.run.getAsBoolean(); } catch (Exception e) { ok = false; }
            if (ok) { System.out.println("  PASS   " + c.name); corePass++; }
            else System.out.println("  FAIL   " + c.name);
        }
        System.out.println("=".repeat(40));
        System.out.println("  SCORE: " + corePass + "/" + coreTotal + " cold");

        if (corePass == coreTotal && coreTotal > 0) {
            if (fresh) { System.out.println("  TIME:  timer only started this run - code from the stubs to clock a real session"); Files.deleteIfExists(mark); }
            else { System.out.println("  TIME:  " + fmt(elapsed)); Files.deleteIfExists(mark); }
        } else {
            System.out.println("  ELAPSED: " + fmt(elapsed) + " so far");
        }

        int bonusPass = 0, bonusTotal = 0;
        for (Case c : cs) if (!c.core) { bonusTotal++; boolean ok; try { ok = c.run.getAsBoolean(); } catch (Exception e) { ok = false; } if (ok) bonusPass++; }
        if (bonusTotal > 0) {
            System.out.println("- ".repeat(20));
            System.out.println("  BONUS (not scored): " + bonusPass + "/" + bonusTotal);
            for (Case c : cs) if (!c.core) { boolean ok; try { ok = c.run.getAsBoolean(); } catch (Exception e) { ok = false; } System.out.println("    " + (ok ? "pass" : "fail") + "   " + c.name); }
        }
        System.out.println("=".repeat(40) + "\n");
    }
}
