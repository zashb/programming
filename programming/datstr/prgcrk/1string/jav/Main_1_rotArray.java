import java.io.*;
import java.util.Arrays;
import java.lang.Object;

/**
 * Main_1_rotArray
 * 
 */
class Main_1_rotArray{
    public static void reverse(int[]nums,int k){
        int[]p1=Arrays.copyOfRange(nums,nums.length-k, nums.length);
        int[]p2=Arrays.copyOfRange(nums,0,k+1);
        int[]res=new int[p1.length+p2.length];
        System.arraycopy(p1, 0, res, 0, p1.length);
        System.arraycopy(p2, 0, res, p1.length,p2.length);
        for (int i : res) {
            System.out.println(i);
        }
    }
    public static void main(String[] args) {
        Main_1_rotArray main_1_rotArray = new Main_1_rotArray();
        int[] nums={1,2,3,4,5,6,7};
        int k=3;
        main_1_rotArray.reverse(nums, k);
    }
}