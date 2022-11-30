class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d={}
        #s=set()
        s=set(arr)
        for i in range(len(arr)):
            if arr[i] in d:
                d[arr[i]]+=1
            else:
                d[arr[i]]=1
        u=[]     
        for i in d:
            u.append(d[i])
        q=set(u)
        if len(u)==len(q):
            return True
        else:
            return False
        

           