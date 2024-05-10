function findMiddleIndex(nums: number[]): number {
    let middleIndex = 0; // start from the beginning
    let leftSum = 0; // If middleIndex == 0, the left side sum is considered to be 0.
    let rightSum = nums.reduce((acc, current) => acc + current, 0) - nums[middleIndex];
    
    while (middleIndex < nums.length) {
        if (rightSum === leftSum) return middleIndex;

        let current = nums[middleIndex];
        let next = nums[middleIndex + 1];

        middleIndex++;
        leftSum += current;
        rightSum -= next;
    }
    
    return -1;
}