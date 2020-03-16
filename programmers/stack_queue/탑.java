class Solution {
    public int[] solution(int[] heights) {
        int[] answer = new int[heights.length]; // 0���� ��� �ʱ�ȭ�ȴ�.
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