#include <iostream>
#include <vector>
using namespace std;
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);   
    cout.tie(NULL);

    int N;
    cin >> N;
    for (int i = 0;i < N;i++) {
        vector<int> v;
        string s;
        cin >> s;
        for (int j = 0;j < s.length();j++) {
            if (v.size() > 0) {
                if(v.back() == '(' && s[j] == ')')
                    v.pop_back();
                else
                    v.push_back(s[j]);
            }else
                v.push_back(s[j]);
        }
        if (v.size() > 0)
            cout << "NO\n";
        else
            cout << "YES\n";
    }
}