class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        for(int i=m,j=0; i<nums1.size(); i++)
        {
            nums1[i] = nums2[j];
            j++;
        }
        for(int i=0; i<nums1.size()-1; i++)
        {
            for(int j=i+1; j<=nums1.size()-1; j++)
            {
                if(nums1[i] > nums1[j])
                {
                    int temp = nums1[i];
                    nums1[i] = nums1[j];
                    nums1[j] = temp;
                }
            }
        }
    }
};