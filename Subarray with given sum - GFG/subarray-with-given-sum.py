#User function Template for python3

#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self,arr, n, s):
        sum1=0
        window_start=0
        l=[]
        flag=False
        for window_end in range(n):
            if flag:
                break
            sum1+=arr[window_end]
            while sum1>s:
                sum1-=arr[window_start]
                window_start+=1
            if sum1==s:
                l.append(window_start+1)
                l.append(window_end+1)
                flag=True
                break
        if len(l)==0 or s==0:
            return [-1]
        return l    
        # windowstart=0
        # for windowend in range(len(arr)):
        #     sum1+=arr[windowend]
        #     if sum1==s:
        #         print(windowend-windowstart,windowend)
        #     elif sum1>s:
        #         sum1-=arr[windowstart]
        #         windowstart+=1
    
       #Write your code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            NS=input().strip().split()
            N=int(NS[0])
            S=int(NS[1])
            
            A=list(map(int,input().split()))
            ob=Solution()
            ans=ob.subArraySum(A, N, S)
            
            for i in ans:
                print(i, end=" ")
                
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends