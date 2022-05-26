class Solution {
public:
    bool checkIfExist(vector<int>& arr) {
        bool doFound = false;
        double div;
        for(int i=0; i<arr.size()-1; i++)
        {
            for(int j=0; j<arr.size(); j++)
            {
                if(arr[j] == 2*arr[i] || arr[i] == 2*arr[j])
                {
                    if(i == j)
                    {
                        // do nothing
                    }
                    else
                    {
                        doFound = true;
                        cout << arr[j] << " " << arr[i] << endl;
                        break;
                    }
                }
            }
            if(doFound == true)
            {
                break;
            }
        }
        return doFound;
    }
};