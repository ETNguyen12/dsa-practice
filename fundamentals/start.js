/*
 * DRILL GENERATOR + TEST RUNNER (JavaScript)  - mirrors start.py
 *
 * Daily workflow:
 *   1. node start.js
 *      -> stamps a fresh MM-DD-YYYY.js (stubs only) beside start.js.
 *      -> if today's file exists, stamps MM-DD-YYYY_2.js, _3.js, ...
 *      -> running start.js does NOT start any timer.
 *   2. Fill in the functions, then:  node MM-DD-YYYY.js
 *      -> the clock starts on that first run and persists across re-runs.
 *   3. On a timed full clear of the CORE set, earlier days' files are deleted.
 *
 * To re-tier: move a name between CORE / BONUS / DEPRECATED below.
 */

const fs = require("fs");
const path = require("path");

// ============================================================================
// EDIT HERE
// ============================================================================
const CORE = [
  "reverseList", "deleteMiddleNode", "oddEvenList",
  "dfsIterative", "bfs", "dfsRecursive",
  "topK",
  "binarySearch", "lowerBound",
  "maxWindowSum", "longestUniqueSubstring",
  "maxDepth", "levelOrder", "isValidBst", "searchBst",
  "groupAnagrams",
  "numIslands",
  "threeSum", "dailyTemperatures",
  "mergeIntervals",
  "deleteBstNode",
  "subsets",
  "minEatingSpeed",
  "subarraySum",
];
const BONUS = ["coinChange", "courseSchedule", "uniquePaths", "diameterOfBinaryTree"];
const DEPRECATED = ["findMiddle", "hasCycle"];
// ============================================================================

class ListNode { constructor(val = 0, next = null) { this.val = val; this.next = next; } }
class TreeNode { constructor(val = 0, left = null, right = null) { this.val = val; this.left = left; this.right = right; } }

// --- test helpers -----------------------------------------------------------
const buildL = (v) => { const d = new ListNode(); let c = d; for (const x of v) { c.next = new ListNode(x); c = c.next; } return d.next; };
const toL = (h) => { const o = []; while (h) { o.push(h.val); h = h.next; } return o; };
function buildT(v, NIL = null) {
  if (!v.length || v[0] === NIL) return null;
  const root = new TreeNode(v[0]); const q = [root]; let i = 1;
  while (q.length && i < v.length) {
    const n = q.shift();
    if (i < v.length) { if (v[i] !== NIL) { n.left = new TreeNode(v[i]); q.push(n.left); } i++; }
    if (i < v.length) { if (v[i] !== NIL) { n.right = new TreeNode(v[i]); q.push(n.right); } i++; }
  }
  return root;
}
const inorder = (r) => { const o = []; (function go(n) { if (!n) return; go(n.left); o.push(n.val); go(n.right); })(r); return o; };
const eq = (a, b) => JSON.stringify(a) === JSON.stringify(b);
const normI = (xss) => xss.map((x) => [...x].sort((a, b) => a - b)).sort((a, b) => JSON.stringify(a).localeCompare(JSON.stringify(b)));
const normS = (gs) => gs.map((g) => [...g].sort()).sort((a, b) => JSON.stringify(a).localeCompare(JSON.stringify(b)));
const G = { 0: [1, 2], 1: [0, 3], 2: [0, 3], 3: [1, 2] };

// --- the registry: sig + desc + test for every problem ----------------------
const PROBLEMS = {
  reverseList: { sig: "reverseList(head)", desc: "Reverse a linked list. Return the new head.",
    test: (f) => eq(toL(f(buildL([1, 2, 3, 4, 5]))), [5, 4, 3, 2, 1]) && eq(toL(f(buildL([]))), []) && eq(toL(f(buildL([1]))), [1]) },
  deleteMiddleNode: { sig: "deleteMiddleNode(head)", desc: "Delete the middle node (floor(n/2)-th, 0-indexed). [1,2,3,4]->[1,2,4]. [1]->[].",
    test: (f) => eq(toL(f(buildL([1, 3, 4, 7, 1, 2, 6]))), [1, 3, 4, 1, 2, 6]) && eq(toL(f(buildL([1, 2, 3, 4]))), [1, 2, 4]) && eq(toL(f(buildL([2, 1]))), [2]) && eq(toL(f(buildL([1]))), []) },
  oddEvenList: { sig: "oddEvenList(head)", desc: "Regroup odd POSITIONS first, then even, preserving order. [1,2,3,4,5]->[1,3,5,2,4].",
    test: (f) => eq(toL(f(buildL([1, 2, 3, 4, 5]))), [1, 3, 5, 2, 4]) && eq(toL(f(buildL([2, 1, 3, 5, 6, 4, 7]))), [2, 3, 6, 7, 1, 5, 4]) && eq(toL(f(buildL([]))), []) && eq(toL(f(buildL([1]))), [1]) },
  bfs: { sig: "bfs(graph, start)", desc: "BFS over an adjacency-list graph. Return first-visit order from start.",
    test: (f) => eq(f(G, 0), [0, 1, 2, 3]) },
  dfsRecursive: { sig: "dfsRecursive(graph, start)", desc: "Recursive DFS. Visit order from start.",
    test: (f) => eq(f(G, 0), [0, 1, 3, 2]) },
  dfsIterative: { sig: "dfsIterative(graph, start)", desc: "Iterative DFS with an explicit stack. Order can differ from recursive.",
    test: (f) => eq(f(G, 0), [0, 2, 3, 1]) },
  topK: { sig: "topK(nums, k)", desc: "The k largest numbers, sorted descending. Use a heap (or sort).",
    test: (f) => eq(f([3, 1, 8, 2, 9, 4], 3), [9, 8, 4]) && eq(f([5], 1), [5]) },
  binarySearch: { sig: "binarySearch(nums, target)", desc: "Index of target in a sorted array, else -1.",
    test: (f) => f([1, 3, 5, 7, 9], 7) === 3 && f([1, 3, 5, 7, 9], 1) === 0 && f([1, 3, 5, 7, 9], 9) === 4 && f([1, 3, 5, 7, 9], 4) === -1 && f([], 1) === -1 },
  lowerBound: { sig: "lowerBound(nums, target)", desc: "Index of the first element >= target. [1,3,3,5],3->1. 6->4. 0->0.",
    test: (f) => f([1, 3, 3, 5], 3) === 1 && f([1, 3, 3, 5], 4) === 3 && f([1, 3, 3, 5], 6) === 4 && f([1, 3, 3, 5], 0) === 0 },
  maxWindowSum: { sig: "maxWindowSum(nums, k)", desc: "Max sum of any window of size k, in one pass.",
    test: (f) => f([2, 1, 5, 1, 3, 2], 3) === 9 && f([1, 2, 3], 3) === 6 && f([4], 1) === 4 },
  longestUniqueSubstring: { sig: "longestUniqueSubstring(s)", desc: 'Length of the longest substring with no repeats. "abcabcbb"->3.',
    test: (f) => f("abcabcbb") === 3 && f("bbbbb") === 1 && f("pwwkew") === 3 && f("") === 0 },
  maxDepth: { sig: "maxDepth(root)", desc: "Max depth of a binary tree. Empty -> 0.",
    test: (f) => f(buildT([3, 9, 20, null, null, 15, 7])) === 3 && f(buildT([])) === 0 && f(buildT([1])) === 1 },
  levelOrder: { sig: "levelOrder(root)", desc: "Level-order -> list of levels. [3,9,20,null,null,15,7]->[[3],[9,20],[15,7]].",
    test: (f) => eq(f(buildT([3, 9, 20, null, null, 15, 7])), [[3], [9, 20], [15, 7]]) && eq(f(buildT([])), []) && eq(f(buildT([1])), [[1]]) },
  isValidBst: { sig: "isValidBst(root)", desc: "True if a valid BST (strict, bounded by ancestors).",
    test: (f) => f(buildT([2, 1, 3])) === true && f(buildT([5, 1, 4, null, null, 3, 6])) === false && f(buildT([5, 4, 6, null, null, 3, 7])) === false && f(buildT([1])) === true },
  searchBst: { sig: "searchBst(root, val)", desc: "Return the subtree whose value == val, else null. Use the BST property.",
    test: (f) => { const r = f(buildT([4, 2, 7, 1, 3]), 2); return r && r.val === 2 && eq(inorder(r), [1, 2, 3]) && f(buildT([4, 2, 7, 1, 3]), 5) === null; } },
  groupAnagrams: { sig: "groupAnagrams(strs)", desc: "Group anagrams together. Key each word by its sorted letters.",
    test: (f) => eq(normS(f(["eat", "tea", "tan", "ate", "nat", "bat"])), normS([["eat", "tea", "ate"], ["tan", "nat"], ["bat"]])) },
  numIslands: { sig: "numIslands(grid)", desc: "Count 4-directionally connected islands of 1s in a 2D grid.",
    test: (f) => f([[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 1]]) === 3 && f([[1, 1, 1, 1, 0], [1, 1, 0, 1, 0], [1, 1, 0, 0, 0], [0, 0, 0, 0, 0]]) === 1 && f([[0, 0], [0, 0]]) === 0 },
  threeSum: { sig: "threeSum(nums)", desc: "All unique triplets summing to 0. [-1,0,1,2,-1,-4]->[[-1,-1,2],[-1,0,1]].",
    test: (f) => eq(normI(f([-1, 0, 1, 2, -1, -4])), normI([[-1, -1, 2], [-1, 0, 1]])) && eq(normI(f([0, 0, 0])), normI([[0, 0, 0]])) && eq(f([0, 1, 1]), []) },
  dailyTemperatures: { sig: "dailyTemperatures(temperatures)", desc: "Days until a warmer temp (0 if none). [73,74,75,71,69,72,76,73]->[1,1,4,2,1,1,0,0].",
    test: (f) => eq(f([73, 74, 75, 71, 69, 72, 76, 73]), [1, 1, 4, 2, 1, 1, 0, 0]) && eq(f([30, 40, 50, 60]), [1, 1, 1, 0]) && eq(f([30, 60, 90]), [1, 1, 0]) },
  mergeIntervals: { sig: "mergeIntervals(intervals)", desc: "Merge overlapping [start,end] intervals. [[1,3],[2,6],[8,10]]->[[1,6],[8,10]].",
    test: (f) => eq(f([[1, 3], [2, 6], [8, 10], [15, 18]]), [[1, 6], [8, 10], [15, 18]]) && eq(f([[1, 4], [4, 5]]), [[1, 5]]) && eq(f([[1, 4], [0, 2], [3, 5]]), [[0, 5]]) },
  deleteBstNode: { sig: "deleteBstNode(root, key)", desc: "Delete node with value key; return the (possibly new) root, keeping BST valid.",
    test: (f) => eq(inorder(f(buildT([5, 3, 6, 2, 4, null, 7]), 3)), [2, 4, 5, 6, 7]) && eq(inorder(f(buildT([5, 3, 6, 2, 4, null, 7]), 7)), [2, 3, 4, 5, 6]) && eq(inorder(f(buildT([5, 3, 6, 2, 4, null, 7]), 5)), [2, 3, 4, 6, 7]) && eq(inorder(f(buildT([1]), 1)), []) },
  subsets: { sig: "subsets(nums)", desc: "Power set of distinct nums. Order free.",
    test: (f) => eq(normI(f([1, 2, 3])), normI([[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]])) && eq(normI(f([])), [[]]) && eq(normI(f([0])), normI([[], [0]])) },
  minEatingSpeed: { sig: "minEatingSpeed(piles, h)", desc: "Smallest integer speed to eat all piles within h hours. ([3,6,7,11],8)->4.",
    test: (f) => f([3, 6, 7, 11], 8) === 4 && f([30, 11, 23, 4, 20], 5) === 30 && f([30, 11, 23, 4, 20], 6) === 23 },
  subarraySum: { sig: "subarraySum(nums, k)", desc: "Count subarrays whose sum equals k. Seed {0:1}. ([1,1,1],2)->2.",
    test: (f) => f([1, 1, 1], 2) === 2 && f([1, 2, 3], 3) === 2 && f([1, -1, 0], 0) === 3 },
  coinChange: { sig: "coinChange(coins, amount)", desc: "Fewest coins summing to amount, or -1. ([1,2,5],11)->3.",
    test: (f) => f([1, 2, 5], 11) === 3 && f([2], 3) === -1 && f([1], 0) === 0 && f([1, 5, 10, 25], 30) === 2 },
  courseSchedule: { sig: "courseSchedule(numCourses, prerequisites)", desc: "True if all courses can finish (no cycle). [a,b] means b before a.",
    test: (f) => f(2, [[1, 0]]) === true && f(2, [[1, 0], [0, 1]]) === false && f(4, [[1, 0], [2, 1], [3, 2]]) === true },
  uniquePaths: { sig: "uniquePaths(m, n)", desc: "Unique right/down paths in an m x n grid. (3,7)->28.",
    test: (f) => f(3, 7) === 28 && f(3, 2) === 3 && f(1, 1) === 1 },
  diameterOfBinaryTree: { sig: "diameterOfBinaryTree(root)", desc: "Edges on the longest path between any two nodes. ([1,2,3,4,5])->3.",
    test: (f) => f(buildT([1, 2, 3, 4, 5])) === 3 && f(buildT([1])) === 0 && f(buildT([1, 2])) === 1 },
  findMiddle: { sig: "findMiddle(head)", desc: "Middle node (second middle on even length). Fast/slow.",
    test: (f) => f(buildL([1, 2, 3, 4, 5])).val === 3 && f(buildL([1, 2, 3, 4])).val === 3 },
  hasCycle: { sig: "hasCycle(head)", desc: "Detect a cycle. Fast/slow.",
    test: (f) => { const a = new ListNode(1), b = new ListNode(2), c = new ListNode(3); a.next = b; b.next = c; c.next = a; return f(a) === true && f(buildL([1, 2, 3])) === false; } },
};

// --- runner -----------------------------------------------------------------
function fmt(sec) { const m = Math.floor(sec / 60), s = Math.floor(sec % 60); return `${m}m ${String(s).padStart(2, "0")}s`; }

function runSet(names, fns, scored) {
  const out = [];
  for (const key of names) {
    if (!(key in PROBLEMS)) { out.push([key, "not in PROBLEMS"]); continue; }
    const fn = fns[key];
    if (typeof fn !== "function") { if (scored) out.push([key, "absent (stub deleted?)"]); continue; }
    try { out.push([key, PROBLEMS[key].test(fn) === true]); }
    catch (e) { out.push([key, `crashed: ${e.message}`]); }
  }
  return out;
}

function runDrills(fns, dailyPath) {
  const startFile = path.join(path.dirname(dailyPath), "." + path.basename(dailyPath) + ".start");
  const core = runSet(CORE, fns, true);
  const bonus = runSet(BONUS, fns, false);

  let start, fresh;
  if (fs.existsSync(startFile)) { start = parseFloat(fs.readFileSync(startFile, "utf8")); fresh = false; }
  else { start = Date.now() / 1000; fresh = true; fs.writeFileSync(startFile, String(start)); }
  const elapsed = Date.now() / 1000 - start;

  console.log("\n" + "=".repeat(40));
  let passed = 0;
  for (const [name, res] of core) {
    if (res === true) { console.log(`  PASS   ${name}`); passed++; }
    else if (res === false) console.log(`  FAIL   ${name}  (wrong output)`);
    else console.log(`  ERROR  ${name}  (${res})`);
  }
  console.log("=".repeat(40));
  console.log(`  SCORE: ${passed}/${core.length} cold`);

  if (passed === core.length && core.length > 0) {
    if (fresh) { console.log("  TIME:  timer only started this run - code from the stubs to clock a real session"); fs.unlinkSync(startFile); }
    else { console.log(`  TIME:  ${fmt(elapsed)}`); fs.unlinkSync(startFile); const removed = sweepOthers(dailyPath); if (removed.length) console.log(`  CLEANED: removed earlier day(s): ${removed.join(", ")}`); }
  } else {
    console.log(`  ELAPSED: ${fmt(elapsed)} so far`);
  }

  if (bonus.length) {
    const bpass = bonus.filter(([, r]) => r === true).length;
    console.log("- ".repeat(20));
    console.log(`  BONUS (not scored): ${bpass}/${bonus.length}`);
    for (const [name, res] of bonus) console.log(`    ${res === true ? "pass" : res === false ? "fail" : "err "}   ${name}`);
  }
  console.log("=".repeat(40) + "\n");
}

const DAILY_RE = /^(\d{2}-\d{2}-\d{4})(?:_\d+)?\.js$/;
function sweepOthers(currentFile) {
  const folder = path.dirname(path.resolve(currentFile));
  const keep = path.basename(currentFile);
  const curStem = (DAILY_RE.exec(keep) || [])[1];
  const removed = [];
  for (const fn of fs.readdirSync(folder)) {
    const m = DAILY_RE.exec(fn);
    if (!m || fn === keep || m[1] === curStem) continue;
    try { fs.unlinkSync(path.join(folder, fn)); const mk = path.join(folder, "." + fn + ".start"); if (fs.existsSync(mk)) fs.unlinkSync(mk); removed.push(fn); } catch (e) {}
  }
  return removed;
}

// --- stamper ----------------------------------------------------------------
function renderStub(label, spec) {
  const bar = "// " + "=".repeat(74);
  const descLines = spec.desc.split("\n");
  const body = [bar, `// ${label}. ${descLines[0]}`];
  for (const ln of descLines.slice(1)) body.push(ln ? `//     ${ln}` : "//");
  body.push(bar);
  body.push(`function ${spec.sig} {`);
  body.push("  // your code");
  body.push("}");
  return body.join("\n");
}

function stampToday() {
  const here = __dirname;
  const d = new Date();
  const stem = `${String(d.getMonth() + 1).padStart(2, "0")}-${String(d.getDate()).padStart(2, "0")}-${d.getFullYear()}`;
  let out = path.join(here, stem + ".js"), nth = 1;
  while (fs.existsSync(out)) { nth++; out = path.join(here, `${stem}_${nth}.js`); }

  const header = `/*
 * ${stem} - DSA drills. Fill in each function from memory, then:  node ${path.basename(out)}
 * No reference until you've been stuck >90 seconds. On a peek, retype the WHOLE function.
 */
const { runDrills, ListNode, TreeNode } = require("./start.js");


`;
  const blocks = [];
  CORE.forEach((k, i) => { if (PROBLEMS[k]) blocks.push(renderStub(String(i + 1), PROBLEMS[k])); });
  if (BONUS.length) {
    blocks.push("// " + "\u2588".repeat(74) + "\n// BONUS - extra reps; not scored, never gate the timer.\n// " + "\u2588".repeat(74));
    BONUS.forEach((k, j) => { if (PROBLEMS[k]) blocks.push(renderStub(`B${j + 1}`, PROBLEMS[k])); });
  }
  const names = [...CORE, ...BONUS].filter((k) => PROBLEMS[k]).join(", ");
  const footer = `\n\n\nrunDrills({ ${names} }, __filename);\n`;
  fs.writeFileSync(out, header + blocks.join("\n\n\n") + footer);

  console.log(`\n  Stamped  ${path.basename(out)}${nth > 1 ? `  - attempt #${nth} for today` : ""}  (${CORE.length} core + ${BONUS.length} bonus)`);
  console.log(`  Fill it in, then run:  node ${path.basename(out)}   (timer starts on that run, not now)\n`);
}

module.exports = { runDrills, ListNode, TreeNode, PROBLEMS, CORE, BONUS, DEPRECATED };

if (require.main === module) stampToday();
