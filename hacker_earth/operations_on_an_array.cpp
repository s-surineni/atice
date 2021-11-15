// https://www.hackerearth.com/practice/data-structures/advanced-data-structures/fenwick-binary-indexed-trees/practice-problems/algorithm/kth-element-2-7d970b44/description/
#include <iostream>
#include <vector>
#include <cmath>
using namespace std;
const int N = 1000000 + 1;
int arr[N];
struct BIT{//use one based indexing
  int N;
  vector<int> bit;
  void init(int n){
    bit.clear();
    N = n + 9;
    bit.assign(n + 10, 0);
  }
  void update(int idx, int val){
    while(idx <= N){
      bit[idx] += val;
      idx += idx & -idx;
    }
  }
  int pref(int idx){
    int ans = 0;
    while(idx > 0){
      ans += bit[idx];
      idx -= idx & -idx;
    }
    return ans;
  }
  int rsum(int l, int r){
    return pref(r) - pref(l - 1);
  }
  int kthOrder(int k){
    if(pref(N - 1) < k){
      return -1;
    }
    int cur = 0,sum = 0, ExtraSize = N;
    int ln = log2(ExtraSize);
    for(int i = ln;i >= 0 ; --i){
      int temp = cur + (1 << i);
      if((temp < ExtraSize) && (sum + bit[temp]) < k){
        cur = temp;
        sum += bit[temp];
      }
    }
    return cur + 1;
  }
  //one based indexing
  int lower_bound(int val){
    return (pref(val - 1) + 1);
  }
  //one based indexing
  int upper_bound(int val){
    return (pref(val) + 1);
  }
}bt;
signed main(){
  ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
  int n,x;
  cin >> n >> x;
  bt.init(n);
  for(int i = 1;i <= n;i++){
    cin >> arr[i];
    if(arr[i] == x){
      bt.update(i,1);
    }
  }
  int q;
  cin >> q;
  while(q--){
    int type;
    cin >> type;
    if(type == 1){
      int l,r,k;
      cin >> l >> r >> k;
      k += bt.pref(l - 1);
      if(k > bt.pref(r)){
        cout << "-1\n";;
        continue;
      }
      cout << bt.kthOrder(k) << "\n";
    }else{
      int l,val;
      cin >> l >> val;
      if(arr[l] == x){
        bt.update(l,-1);
      }
      if(val == x){
        bt.update(l,1);
      }
      arr[l] = val;
    }
  }
}
