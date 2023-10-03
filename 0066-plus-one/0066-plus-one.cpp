class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int s=digits.size();
        int f=0,i;
        if (digits[s-1]==9)
        f=1;
        if(f==0)
        digits[s-1]++;
        else
        {
            int sum;
            int c=1;
            for(i=s-1;i>=0;i--)
            {
                sum=digits[i]+c;
                digits[i]=sum%10;
                c=sum/10;
                if(c==0)
                break;
            }
            if(c>0)
            {
            digits.insert(digits.begin(),c);
            }
        }
        return digits;
    }
};