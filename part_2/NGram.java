import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapreduce.*;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

import java.io.IOException;

public class NGram {

    // mapper
    public static class NGramMapper extends Mapper<LongWritable, Text, Text, IntWritable> {
        
        private final static IntWritable one = new IntWritable(1);
        private Text ngramText = new Text();
        private int n;

        @Override
        protected void setup(Context context) {
            // get n from config
            Configuration conf = context.getConfiguration();
            n = conf.getInt("ngram.n", 2); // default n=2
        }

        @Override
        public void map(LongWritable key, Text value, Context context) 
                throws IOException, InterruptedException {
            
            String line = value.toString();
            
            // generate all n-grams from this line
            for (int i = 0; i <= line.length() - n; i++) {
                String ngram = line.substring(i, i + n);
                ngramText.set(ngram);
                context.write(ngramText, one);
            }
        }
    }

    // reducer
    public static class NGramReducer extends Reducer<Text, IntWritable, Text, IntWritable> {
        
        private IntWritable result = new IntWritable();

        @Override
        public void reduce(Text key, Iterable<IntWritable> values, Context context)
                throws IOException, InterruptedException {
            
            int sum = 0;
            for (IntWritable val : values) {
                sum += val.get();
            }
            result.set(sum);
            context.write(key, result);
        }
    }

    // main
    public static void main(String[] args) throws Exception {
        
        if (args.length < 3) {
            System.err.println("Usage: NGram <n> <input path> <output path>");
            System.exit(-1);
        }

        Configuration conf = new Configuration();
        
        //set n from command line
        int n = Integer.parseInt(args[0]);
        conf.setInt("ngram.n", n);

        Job job = Job.getInstance(conf, "N-Gram Count");
        job.setJarByClass(NGram.class);
        
        //mapper and reducer
        job.setMapperClass(NGramMapper.class);
        job.setCombinerClass(NGramReducer.class);
        job.setReducerClass(NGramReducer.class);

        //output key/value types
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);

        //input and output paths
        FileInputFormat.addInputPath(job, new Path(args[1]));
        FileOutputFormat.setOutputPath(job, new Path(args[2]));

        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}