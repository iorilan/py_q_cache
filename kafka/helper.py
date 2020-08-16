from kafka import KafkaConsumer
from kafka import KafkaProducer,TopicPartition,ConsumerRebalanceListener

"""
    everything from begnning
    at least once
"""
def consume_from_beginning(host='192.168.11.137:9092',topic='first_topic'):
    consumer = KafkaConsumer(group_id='1',bootstrap_servers=host, auto_offset_reset='earliest',
    enable_auto_commit=True,
    auto_commit_interval_ms=3000)
    
    tp=TopicPartition(topic,0)
    consumer.assign([tp])
    consumer.poll()
    consumer.seek_to_beginning(tp)
    for msg in consumer:
        print (msg)


"""
    only new message
    at least once
"""
def consume_at_least_once(host='192.168.11.137:9092',topic='first_topic'):
    consumer = KafkaConsumer(group_id='1',bootstrap_servers=host, auto_offset_reset='earliest',
    enable_auto_commit=True,
    auto_commit_interval_ms=3000)
    
    """
        only consumer new message
        0 is the default partition id
    """
    tp=TopicPartition(topic,0)
    consumer.assign([tp])
    consumer.poll()
    consumer.seek_to_end(tp)
    for msg in consumer:
        print (msg)

"""
    only new message
    exact once
"""

def consume_exact_once(host='192.168.11.137:9092',topic='first_topic', only_new=True):
    consumer = KafkaConsumer(group_id='1',bootstrap_servers=host)
    consumer.subscribe(topic,listener=CRL(consumer))
    consumer.poll()
    
    for tp in consumer.assignment():
        offset=0
        if tp.partition in CRL.mem_db:
            offset = CRL.mem_db[tp.partition]
            consumer.seek(tp, offset)
        else:
            consumer.seek_to_end(tp)
    while True:
        message_batch = consumer.poll()

        for topic_partition, partition_batch in message_batch.items():
            for message in partition_batch:
                print(message)
                CRL.mem_db[topic.partition]=message.offset

def produce(msg, host='192.168.11.137:9092',topic='first_topic'):

    producer = KafkaProducer(bootstrap_servers=host)
    future = producer.send(topic, partition=0, value= msg.encode('utf-8'))
    try:
        record_metadata = future.get(timeout=10)
    except KafkaError:
        # Decide what to do if produce request failed...
        log.exception()
        pass

    # Successful result returns assigned partition and offset
    print (record_metadata.topic)
    print (record_metadata.partition)
    print (record_metadata.offset)

class CRL(ConsumerRebalanceListener):
    #simulate db 
    mem_db = {}
    def __init__(self, consumer):
        self.consumer = consumer

    def on_partitions_revoked(self, revoked):
        pass

    def on_partitions_assigned(self, assigned):
        # on a rebalancing of partitions this method will be called if a new partition is assigned to this consumer
        for topic_partition in assigned:
            self.consumer.seek(topic_partition.partition, CRL.mem_db[topic_partition.partition])