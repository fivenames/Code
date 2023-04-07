import org.apache.commons.csv.CSVFormat;
import org.apache.commons.csv.CSVParser;
import org.apache.commons.csv.CSVRecord;
import java.io.Reader;
import java.io.FileReader;

public class Country {

    public static CSVParser init_parser(String filename){
        Reader reader = new FileReader(filename);
        CSVParser csvParser = new CSVParser(reader, CSVFormat.DEFAULT);
        return csvParser;
    }

    public static String country_info(CSVParser parser, String country){
        for (CSVRecord record : parser) {
            String str = record.get("Country");
            if(str.equals(country)){
                return String.format("%s : %s : %s", str, record.get("Export"), record.get("Value (dollars)"));
            }
        }
        return "Country not found";
    }

    public static void find_by_export(CSVParser parser, String... args){
        for(CSVRecord record : parser){
            String str = record.get("Export");
            int i = args.length;
            int correct_count = 0;

            for(String arg : args){
            if (str.contains(arg)){
                correct_count++;
            }
            else{
                break;
            }

            if(correct_count == i){
                System.out.println(record.get("Country"));
            }
        }
        }
    }

    public static int number_exporters(CSVParser parser, String export){
        int exporter;
        for(CSVRecord record : parser){
            String exports = record.get("Exports");
            if(exports.contains(export)){
                exporter++;
            }
        }
        return exporter;
    }

    public static void big_exporters(CSVParser parser, String amount){
        int i = amount.length();

        for(CSVRecord record : parser){
            String value = record.get("Value (dollars)");
            if(value.length() >= i){
                System.out.println(record.get("Country"));
            }
        }
    }

    public static void main(String[] args){
        CSVParser parser = init_parser("exportdata.csv");
        find_by_export(parser, "fish", "nuts");
        parser.close();
    }
}

