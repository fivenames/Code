import java.util.Map;
import java.util.HashMap;
import java.util.ArrayList;

public class Gene {
    private String sequence;

    public Gene (String init_seq) {
        sequence = init_seq.toUpperCase();
    }

    public String find(){
        String startcodon = "ATG";
        String[] stopcodons = {"TAA", "TAG", "TGA"};
        // Initialise a Map Class Object, implementing a dict data struct by calling HashMap constructor.
        Map<String, Integer> dict = new HashMap<String, Integer>();

        int startidx = this.sequence.indexOf(startcodon);
        int endidx = startidx;
        for(String stopcodon : stopcodons){
            while(true){
                endidx = this.sequence.indexOf(stopcodon, endidx + 1);
                if(endidx == -1){
                    break;
                }
                else if((endidx + 3 - startidx) % 3 == 0){
                    dict.put(stopcodon, endidx);
                    break;
                }
            }
        }

        if(dict.isEmpty()){
            return "Not found";
        }

        // Iterate through each element
        Map.Entry<String, Integer> min = null;
        for (Map.Entry<String, Integer> entry : dict.entrySet()){
            if (min == null || min.getValue() > entry.getValue()) {
                min = entry;
            }
        }

        int stopidx = min.getValue();
        String ans = this.sequence.substring(startidx, stopidx + 3);
        return ans;
    }

    public static ArrayList<String> find_all(Gene seq){
        // Resizable array, unlike LinkedList
        ArrayList<String> sequences = new ArrayList<String>();
        while(true){
            String s = seq.find();
            if(s == "Not found"){
                sequences.add("That's all.");
                break;
            }
            sequences.add(s);

            int i = seq.sequence.indexOf(s);
            int len = s.length();
            seq.sequence = seq.sequence.substring(i + len);
        }
        return sequences;
    }

    public static void main(String[] args){
        if(args.length != 1){
            System.out.println("Usage: java Gene sequence");
            return;
        }
        Gene gene = new Gene(args[0]);
        ArrayList<String> list = Gene.find_all(gene);
        for(String str : list){
            System.out.println(str);
        }
    }
}