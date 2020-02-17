class Solution {
    public List<Integer> topKFrequent(int[] nums, int k) {
        HashMap<Integer,Integer> countArray= new HashMap<>();
        PriorityQueue<Freq> heap= new PriorityQueue<>(new freqComp());
        List<Integer> answer= new ArrayList<>();
        for(int i:nums){
            if(countArray.containsKey(i)){
                countArray.put(i,countArray.get(i)+1);
            }else{
                countArray.put(i,1);
            }
        }
        for(int i:countArray.keySet()){
            Freq f= new Freq(i,countArray.get(i));
            if(heap.size()<k){
                heap.add(f);
            }else{
                if(heap.peek().freq<=f.freq){
                    heap.poll();
                    heap.add(f);
                }
            }
        }
        while(heap.size()>0){
            answer.add(heap.poll().num);
        }
        return answer;
    }
}
class Freq{
    int num;
    int freq;
    public Freq(int num,int freq){
        this.num=num;
        this.freq=freq;
    }
}
class freqComp implements Comparator<Freq>{
    @Override
    public int compare(Freq f1,Freq f2){
        if(f1.freq==f2.freq){
            return 0;
        }
        if(f1.freq<f2.freq){
            return -1;
        }
        else{
            return 1;
        }
    }
}
