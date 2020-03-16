class Solution {
    public int[] solution(int[] heights) {
        int[] answer = new int[heights.length]; // 0으로 모두 초기화된다.
        int length = heights.length;
        for (int i = (length-1); i >= 0; i--){
            int value = heights[i];
            for(int j = i-1; j >=0; j--){
                int valueCompared = heights[j];
                if(value < valueCompared){
                    answer[i] = j+1;
                    break;
                }
            }
        }
        return answer;
    }
}
