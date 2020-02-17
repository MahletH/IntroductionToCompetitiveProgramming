class KthLargest {
    PriorityQueue<Integer> heap;
    int K;

    public KthLargest(int k, int[] nums) {
        heap= new PriorityQueue<>();
        this.K=k;
        for(int i=0;i<nums.length;i++){
            if(heap.size()<K){
                heap.add(nums[i]);
            }else{
                if(heap.peek()<nums[i]){
                    heap.poll();
                    heap.add(nums[i]);
                }
            }
        }
        
    }
    
    public int add(int val) {
        if(heap.size()<K){
                heap.add(val);
            }else{
        if(heap.peek()<val){
                heap.poll();
                heap.add(val);
            }
        }
        return heap.peek();

    }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest obj = new KthLargest(k, nums);
 * int param_1 = obj.add(val);
 */
