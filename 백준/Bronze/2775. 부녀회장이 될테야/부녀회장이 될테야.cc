#include <iostream>
using namespace std;

int main() {
    int t;
    cin >> t;
    int dp[15][15] = {0,};
    for(int i = 0; i < 15; i++) {
        dp[0][i] = i;
    }
    for(int i = 0; i < t; i++) {
        int k;
        int n;
        cin >> k >> n;
        if(dp[k][n] != 0) {
            cout << dp[k][n] << endl;
            continue;
        }
        else {
            for(int j = 1; j <= k; j++) {
                for(int l = 1; l <= n; l++) {
                    dp[j][l] = dp[j][l-1] + dp[j-1][l];
                }
            }
            cout << dp[k][n] << endl;
        }
    }
    return 0;
}

