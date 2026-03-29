double findMaxAverage(int* nums, int numsSize, int k) {
    double window_avg = 0;
    double window_total = 0;
    double max_avg = 0;
    for(int i = 0; i < k; i++){
        window_total += nums[i];
    }
    window_avg = window_total/ k;
    max_avg = window_avg;

    for(int i = k; i < numsSize; i++){
        window_total += nums[i] - nums[i-k];
        window_avg = window_total / k;
        if(window_avg > max_avg){
            max_avg = window_avg;
        }
    }
    return max_avg;
}