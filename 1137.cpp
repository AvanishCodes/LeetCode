class Solution {
public:
    int tribonacci(int n) {
        int one = 1, two = 1 ,zero = 0;
        if(n == 0)
            return zero;
        if(n == 1 or n == 2)
            return one;
        int res = zero+one+two;
        for(int i=3; i<=n; i++){
            // int res = 
            res=zero+one+two;
            zero=one;
            one=two;
            two=res;
        }
        return res;
    }
};