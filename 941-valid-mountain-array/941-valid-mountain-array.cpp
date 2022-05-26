class Solution {
public:
    bool validMountainArray(vector<int>& arr) {
        int peak = 0;
        for(int i=0; i<arr.size(); i++)
        {
            if(arr[i] >= arr[peak])
            {
                peak = i;
            }
        }
        cout << "peak is " << peak << endl;
        if(peak == 0 || peak == arr.size()-1 || arr[peak-1] == arr[peak] || arr[peak+1] == arr[peak])
        {
            return false;
        }
        for(int i=peak; i<arr.size()-1; i++)
        {
            if(arr[i+1] >= arr[i])
            {
                return false;
            }
        }
        for(int i=peak; i>0; i--)
        {
            if(arr[i-1] >= arr[i])
            {
                return false;
            }
        }
        return true;
    }
};