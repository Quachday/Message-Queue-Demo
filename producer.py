import pika

# Tạo kết nối đến RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Đảm bảo rằng queue có sẵn trên server
channel.queue_declare(queue='hello')

# Gửi message
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello, World!')
while True:
    
    x = str(input("Write something to the consumer: "))
    # Gửi message
    channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=x)
    print("producer sent: " + str(x))

# Đóng kết nối
connection.close()
