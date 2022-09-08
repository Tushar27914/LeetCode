class Solution {
public:
    int jump(vector<int>& nums) {
        int jumps=0,far=0,curr=0;
        int n=nums.size();
        for(int i=0;i<n-1;i++){
            far=max(far,nums[i]+i);
            if(i==curr){
                curr=far;
                jumps++;
            }
        }
        return jumps;
    }
};