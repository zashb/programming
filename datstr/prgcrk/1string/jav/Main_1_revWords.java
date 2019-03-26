import java.util.*;
/**
 * Main_1_revWords
 */
public class Main_1_revWords {
    public String revWords(String s){
        // // reverse the entire string
        // String rev=new StringBuffer(s).reverse().toString();
        // System.out.println(rev);

        String[] words = s.trim().split(" ");
        // System.out.println(Arrays.toString(words));
        Collections.reverse(Arrays.asList(words));
        String words_rev = String.join(" ",words);
        return words_rev;
    }
    public static void main(String[] args) {
        Main_1_revWords main_1_revWords = new Main_1_revWords();
        String s="the sky is blue";
        System.out.println(main_1_revWords.revWords(s));
    }    
}