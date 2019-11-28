OUTPUT_DIR_AUX=/user/s2002469/assignment/aux_task4
OUTPUT_DIR=/user/s2002469/assignment/task4
OUTPUT_FILE=output.out

# Hadoop won't start if the output directory already exists
hdfs dfs -rm -r $OUTPUT_DIR
hdfs dfs -rm -r $OUTPUT_DIR_AUX

hadoop jar /opt/hadoop/hadoop-2.9.2/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
    -D mapreduce.job.name=${USER}_task4-1 \
    -D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
    -D map.output.key.field.separator="|" \
    -D stream.num.map.output.key.fields=3 \
    -D mapreduce.partition.keypartitioner.options=-k1,1 \
    -D mapreduce.partition.keycomparator.options="-k1,2 -k3" \
    -input /data/large/imdb/title.crew.tsv \
    -input /data/large/imdb/title.ratings.tsv \
    -input /data/large/imdb/name.basics.tsv \
    -output $OUTPUT_DIR_AUX \
    -mapper mapper1.py \
    -reducer reducer1.py \
    -file mapper1.py \
    -file reducer1.py \
    -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner

hadoop jar /opt/hadoop/hadoop-2.9.2/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
    -D mapreduce.job.name=${USER}_task4 \
    -D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
    -D map.output.key.field.separator="|" \
    -D mapred.reduce.tasks=1 \
    -D stream.num.map.output.key.fields=2 \
    -D mapreduce.partition.keycomparator.options="-k1,1nr -k2,2" \
    -input  $OUTPUT_DIR_AUX\
    -output $OUTPUT_DIR \
    -mapper mapper2.py \
    -reducer reducer2.py \
    -combiner combiner2.py \
    -file mapper2.py \
    -file reducer2.py \
    -file combiner2.py \
    -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner


hdfs dfs -cat ${OUTPUT_DIR}/part-* > $OUTPUT_FILE
cat $OUTPUT_FILE
