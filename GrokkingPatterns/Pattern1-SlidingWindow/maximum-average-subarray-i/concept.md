## Problem 623
[Leetcode-623](https://leetcode.com/problems/maximum-average-subarray-i/description/)

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10^-5 will be accepted.

Hint : Contiguous Subarray problems can be solved by Sliding Window

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000

## Brute Force Approach 
bruteforce.py
- Time Complexity : O(NxK)
- Memory Complexity : O(N)

## Sliding Window Approach
maximum_average_subarray.py
- Time Complexity : O(N)
- Memory Complexity : O(N)

### Concept
- Keep updating the averages across the contiguous subarrays and find max in the process. 
- For a subarray of size K, K-1 elements repeat and only one element changes as we go through the contiguous subarrays in a array. Its a sliding window of K elements with K-1 elements repeating. 
- The efficient way to solve this problem would be to visualize each contiguous subarray as a slidingwindow of k elements. This means that we will slide the window by one element when we move on to the next subarray. 
- To reuse the sum from the previous subarray, we will subtract the element going out of the window and add the element now being included in the sliding window. This will save us from going through the whole subarray to find the sum and, as a result, the algorithm complexity will reduce to O(N)
.

