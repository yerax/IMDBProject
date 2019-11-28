OUTPUT_DIR=/user/s2002469/assignment/task2
OUTPUT_FILE=output.out

# Hadoop won't start if the output directory already exists
hdfs dfs -rm -r $OUTPUT_DIR

hadoop jar /opt/hadoop/hadoop-2.9.2/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
    -D mapreduce.job.name=${USER}_task2 \
    -D mapreduce.map.output.key.field.separator="|" \
    -D stream.num.map.output.key.fields=1 \
    -D mapreduce.partition.keypartitioner.options=-k1,1 \
    -D mapreduce.partition.keycomparator.options="k1,1r" \
    -input /data/large/imdb/title.basics.tsv \
    -input /data/large/imdb/title.ratings.tsv \
    -output $OUTPUT_DIR \
    -mapper mapper.py \
    -reducer reducer.py \
    -file mapper.py \
    -file reducer.py \
    -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner

hdfs dfs -cat ${OUTPUT_DIR}/part-* | sort > $OUTPUT_FILE
cat $OUTPUT_FILE
