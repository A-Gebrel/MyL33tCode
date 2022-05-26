

int findNumbers(int* nums, int numsSize){
    int counter = 0;
    int temp = 0;
    for(int i=0; i<numsSize; i++)
    {
        int div = 0;
        temp = nums[i];
        while(temp != 0)
        {
            div++;
            temp /= 10;
        }
        if(div%2 == 0)
        {
            printf("num %d is even digits\n", nums[i]);
            counter++;
        }
    }
    return counter;
}