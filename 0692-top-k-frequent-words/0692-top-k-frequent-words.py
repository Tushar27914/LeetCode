class Solution {
public:
    vector<string> topKFrequent(vector<string>& words, int k) {
        int maxIndex = INT_MIN , minIndex = INT_MAX;
        
        unordered_map<string , int>a;
        vector<vector<string>>b(501 ,vector<string>());
        // frequencyMapping of all words
        for(auto elements:words)
        a[elements]++;
        
        // mapping in auxilaryArray
        for(auto elements:a)
        {
            maxIndex = max(elements.second , maxIndex);
            minIndex = min(elements.second , minIndex);
            b[elements.second].push_back(elements.first);
        }
        vector<string>ans;
        for(int i = maxIndex;i>=minIndex;i--)
        {
              if(b[i].size()>0)
              {
                  if(b[i].size() == 1)
                  {
                      ans.push_back(b[i][0]);
                      k--;
                  }
                  else
                  {  
                      int size = 0;
                     sort(b[i].begin(),b[i].end());
                     while(k > 0  && size < b[i].size())
                     {
                         ans.push_back(b[i][size++]);
                         k--;
                     }
                  }
              }
            if(k == 0)
            return ans;
        }
        return ans;
    }
};