// ============================================================================
// harness.hpp - the C++ drill runner (helpers + tests + timer).
// You don't edit this. Fill in drill.cpp, then:  g++ -std=c++17 drill.cpp -o drill && ./drill
// (or just: ./run.sh). The timer starts on the first ./drill and persists in a
// hidden .drill.start marker across re-runs, resetting on a full CORE clear.
// ============================================================================
#ifndef HARNESS_HPP
#define HARNESS_HPP
#include <bits/stdc++.h>
#include <chrono>
#include <fstream>
using namespace std;

// ---- test helpers ----------------------------------------------------------
static Node* _build(vector<int> vals) {
    Node dummy; Node* cur = &dummy;
    for (int v : vals) { cur->next = new Node(v); cur = cur->next; }
    return dummy.next;
}
static vector<int> _toL(Node* h) { vector<int> o; while (h) { o.push_back(h->val); h = h->next; } return o; }
static const int NIL = -1000;
static TreeNode* _buildT(vector<int> vals) {
    if (vals.empty() || vals[0] == NIL) return nullptr;
    TreeNode* root = new TreeNode(vals[0]);
    queue<TreeNode*> q; q.push(root); size_t i = 1;
    while (!q.empty() && i < vals.size()) {
        TreeNode* n = q.front(); q.pop();
        if (i < vals.size()) { if (vals[i] != NIL) { n->left = new TreeNode(vals[i]); q.push(n->left); } i++; }
        if (i < vals.size()) { if (vals[i] != NIL) { n->right = new TreeNode(vals[i]); q.push(n->right); } i++; }
    }
    return root;
}
static vector<int> _inorder(TreeNode* r) { vector<int> o; function<void(TreeNode*)> go = [&](TreeNode* n){ if(!n)return; go(n->left); o.push_back(n->val); go(n->right); }; go(r); return o; }
template<class T> static vector<T> _sv(vector<T> v){ sort(v.begin(), v.end()); return v; }
static vector<vector<int>> _norm(vector<vector<int>> ts){ for(auto&t:ts)sort(t.begin(),t.end()); sort(ts.begin(),ts.end()); return ts; }

// ---- the test table --------------------------------------------------------
// Each entry: {name, is_core, thunk returning bool}. Order = display order.
struct Case { string name; bool core; function<bool()> run; };

static vector<Case> _cases() {
    unordered_map<int, vector<int>> G = {{0,{1,2}},{1,{0,3}},{2,{0,3}},{3,{1,2}}};
    vector<Case> c;
    auto add = [&](string n, bool core, function<bool()> f){ c.push_back({n, core, f}); };

    add("reverse_list", true, []{ return _toL(reverse_list(_build({1,2,3,4,5}))) == vector<int>({5,4,3,2,1}) && _toL(reverse_list(_build({}))) == vector<int>({}) && _toL(reverse_list(_build({1}))) == vector<int>({1}); });
    add("delete_middle_node", true, []{ return _toL(delete_middle_node(_build({1,3,4,7,1,2,6}))) == vector<int>({1,3,4,1,2,6}) && _toL(delete_middle_node(_build({1,2,3,4}))) == vector<int>({1,2,4}) && _toL(delete_middle_node(_build({2,1}))) == vector<int>({2}) && _toL(delete_middle_node(_build({1}))) == vector<int>({}); });
    add("odd_even_list", true, []{ return _toL(odd_even_list(_build({1,2,3,4,5}))) == vector<int>({1,3,5,2,4}) && _toL(odd_even_list(_build({2,1,3,5,6,4,7}))) == vector<int>({2,3,6,7,1,5,4}) && _toL(odd_even_list(_build({}))) == vector<int>({}) && _toL(odd_even_list(_build({1}))) == vector<int>({1}); });
    add("dfs_iterative", true, [G]() mutable { return dfs_iterative(G,0) == vector<int>({0,2,3,1}); });
    add("bfs", true, [G]() mutable { return bfs(G,0) == vector<int>({0,1,2,3}); });
    add("dfs_recursive", true, [G]() mutable { return dfs_recursive(G,0) == vector<int>({0,1,3,2}); });
    add("top_k", true, []{ return top_k({3,1,8,2,9,4},3) == vector<int>({9,8,4}) && top_k({5},1) == vector<int>({5}); });
    add("binary_search", true, []{ vector<int> a={1,3,5,7,9}, e={}; return binary_search(a,7)==3 && binary_search(a,1)==0 && binary_search(a,9)==4 && binary_search(a,4)==-1 && binary_search(e,1)==-1; });
    add("lower_bound", true, []{ vector<int> a={1,3,3,5}; return lower_bound_idx(a,3)==1 && lower_bound_idx(a,4)==3 && lower_bound_idx(a,6)==4 && lower_bound_idx(a,0)==0; });
    add("max_window_sum", true, []{ vector<int> a={2,1,5,1,3,2}, b={1,2,3}, cc={4}; return max_window_sum(a,3)==9 && max_window_sum(b,3)==6 && max_window_sum(cc,1)==4; });
    add("longest_unique_substring", true, []{ return longest_unique_substring("abcabcbb")==3 && longest_unique_substring("bbbbb")==1 && longest_unique_substring("pwwkew")==3 && longest_unique_substring("")==0; });
    add("max_depth", true, []{ return max_depth(_buildT({3,9,20,NIL,NIL,15,7}))==3 && max_depth(_buildT({}))==0 && max_depth(_buildT({1}))==1; });
    add("level_order", true, []{ return (level_order(_buildT({3,9,20,NIL,NIL,15,7})) == vector<vector<int>>({{3},{9,20},{15,7}})) && level_order(_buildT({})).empty() && (level_order(_buildT({1}))==vector<vector<int>>({{1}})); });
    add("is_valid_bst", true, []{ return is_valid_bst(_buildT({2,1,3}))==true && is_valid_bst(_buildT({5,1,4,NIL,NIL,3,6}))==false && is_valid_bst(_buildT({5,4,6,NIL,NIL,3,7}))==false && is_valid_bst(_buildT({1}))==true; });
    add("search_bst", true, []{ auto r = search_bst(_buildT({4,2,7,1,3}),2); return r && r->val==2 && _inorder(r)==vector<int>({1,2,3}) && search_bst(_buildT({4,2,7,1,3}),5)==nullptr; });
    add("group_anagrams", true, []{ vector<string> in={"eat","tea","tan","ate","nat","bat"}; auto g=group_anagrams(in); vector<vector<string>> nm; for(auto&x:g)nm.push_back(_sv(x)); sort(nm.begin(),nm.end()); vector<vector<string>> ex={{"ate","eat","tea"},{"bat"},{"nat","tan"}}; sort(ex.begin(),ex.end()); return nm==ex; });
    add("num_islands", true, []{ return num_islands({{1,1,0,0,0},{1,1,0,0,0},{0,0,1,0,0},{0,0,0,1,1}})==3 && num_islands({{1,1,1,1,0},{1,1,0,1,0},{1,1,0,0,0},{0,0,0,0,0}})==1 && num_islands({{0,0},{0,0}})==0; });
    add("three_sum", true, []{ return _norm(three_sum({-1,0,1,2,-1,-4}))==_norm({{-1,-1,2},{-1,0,1}}) && _norm(three_sum({0,0,0}))==_norm({{0,0,0}}) && three_sum({0,1,1}).empty(); });
    add("daily_temperatures", true, []{ vector<int> a={73,74,75,71,69,72,76,73}, b={30,40,50,60}, cc={30,60,90}; return daily_temperatures(a)==vector<int>({1,1,4,2,1,1,0,0}) && daily_temperatures(b)==vector<int>({1,1,1,0}) && daily_temperatures(cc)==vector<int>({1,1,0}); });
    add("merge_intervals", true, []{ return merge_intervals({{1,3},{2,6},{8,10},{15,18}})==vector<vector<int>>({{1,6},{8,10},{15,18}}) && merge_intervals({{1,4},{4,5}})==vector<vector<int>>({{1,5}}) && merge_intervals({{1,4},{0,2},{3,5}})==vector<vector<int>>({{0,5}}); });
    add("delete_bst_node", true, []{ return _inorder(delete_bst_node(_buildT({5,3,6,2,4,NIL,7}),3))==vector<int>({2,4,5,6,7}) && _inorder(delete_bst_node(_buildT({5,3,6,2,4,NIL,7}),7))==vector<int>({2,3,4,5,6}) && _inorder(delete_bst_node(_buildT({5,3,6,2,4,NIL,7}),5))==vector<int>({2,3,4,6,7}) && _inorder(delete_bst_node(_buildT({1}),1)).empty(); });
    add("subsets", true, []{ vector<int> a={1,2,3}, e={}, z={0}; return _norm(subsets(a))==_norm({{},{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}}) && _norm(subsets(e))==vector<vector<int>>({{}}) && _norm(subsets(z))==_norm({{},{0}}); });
    add("min_eating_speed", true, []{ vector<int> a={3,6,7,11}, b={30,11,23,4,20}; return min_eating_speed(a,8)==4 && min_eating_speed(b,5)==30 && min_eating_speed(b,6)==23; });
    add("subarray_sum", true, []{ vector<int> a={1,1,1}, b={1,2,3}, cc={1,-1,0}; return subarray_sum(a,2)==2 && subarray_sum(b,3)==2 && subarray_sum(cc,0)==3; });

    add("coin_change", false, []{ vector<int> a={1,2,5}, b={2}, u={1}, m={1,5,10,25}; return coin_change(a,11)==3 && coin_change(b,3)==-1 && coin_change(u,0)==0 && coin_change(m,30)==2; });
    add("course_schedule", false, []{ vector<vector<int>> p1={{1,0}}, p2={{1,0},{0,1}}, p3={{1,0},{2,1},{3,2}}; return course_schedule(2,p1)==true && course_schedule(2,p2)==false && course_schedule(4,p3)==true; });
    add("unique_paths", false, []{ return unique_paths(3,7)==28 && unique_paths(3,2)==3 && unique_paths(1,1)==1; });
    add("diameter_of_binary_tree", false, []{ return diameter_of_binary_tree(_buildT({1,2,3,4,5}))==3 && diameter_of_binary_tree(_buildT({1}))==0 && diameter_of_binary_tree(_buildT({1,2}))==1; });
    return c;
}

// ---- timer + runner --------------------------------------------------------
static string _fmt(double secs){ int m=(int)secs/60, s=(int)secs%60; char buf[32]; snprintf(buf,sizeof buf,"%dm %02ds",m,s); return buf; }

inline int run_drills() {
    const char* MARK = ".drill.start";
    auto cases = _cases();
    int corePass = 0, coreTotal = 0, bonusPass = 0, bonusTotal = 0;

    // timer: read-or-create marker
    double start; bool fresh;
    { ifstream f(MARK); if (f) { f >> start; fresh = false; } else { start = chrono::duration<double>(chrono::system_clock::now().time_since_epoch()).count(); ofstream o(MARK); o << setprecision(17) << start; fresh = true; } }
    double elapsed = chrono::duration<double>(chrono::system_clock::now().time_since_epoch()).count() - start;

    printf("\n%s\n", string(40,'=').c_str());
    for (auto& c : cases) {
        if (!c.core) continue;
        coreTotal++;
        bool ok = false; try { ok = c.run(); } catch (...) { ok = false; }
        if (ok) { printf("  PASS   %s\n", c.name.c_str()); corePass++; }
        else     printf("  FAIL   %s\n", c.name.c_str());
    }
    printf("%s\n", string(40,'=').c_str());
    printf("  SCORE: %d/%d cold\n", corePass, coreTotal);

    if (corePass == coreTotal && coreTotal > 0) {
        if (fresh) { printf("  TIME:  timer only started this run - code from the stubs to clock a real session\n"); remove(MARK); }
        else { printf("  TIME:  %s\n", _fmt(elapsed).c_str()); remove(MARK); }
    } else {
        printf("  ELAPSED: %s so far\n", _fmt(elapsed).c_str());
    }

    for (auto& c : cases) if (!c.core) { bonusTotal++; bool ok=false; try{ ok=c.run(); }catch(...){ok=false;} if(ok)bonusPass++; }
    if (bonusTotal) {
        printf("%s\n", string(40,'-').c_str());
        printf("  BONUS (not scored): %d/%d\n", bonusPass, bonusTotal);
        for (auto& c : cases) if (!c.core) { bool ok=false; try{ok=c.run();}catch(...){ok=false;} printf("    %s   %s\n", ok?"pass":"fail", c.name.c_str()); }
    }
    printf("%s\n\n", string(40,'=').c_str());
    return corePass == coreTotal ? 0 : 1;
}
#endif
