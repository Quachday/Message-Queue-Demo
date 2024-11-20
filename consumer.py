import pika

# Tạo kết nối đến RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Đảm bảo rằng queue có sẵn trên server
channel.queue_declare(queue='hello')

# Hàm callback khi nhận message
def callback(ch, method, properties, body):
    print(f" [x] Received {body}")

# Đăng ký consumer với queue
channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
