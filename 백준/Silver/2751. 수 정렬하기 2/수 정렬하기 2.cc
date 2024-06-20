#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int t;
    int n;
    cin >> t;
    vector<int> v;
    for(int i=0; i<t; i++) {
        cin >> n;
        v.push_back(n);
    }
    sort(v.begin(), v.end());
    for(int i=0; i<t; i++) {
        cout << v[i] << "\n";
    }
    return 0;
}