import hashlib

def calculate_hash(data):
    sha256 = hashlib.sha256(data.encode()).hexdigest()
    return sha256

def All_Data(sender, recipient, subject, body, non, difficulty):
    attempts = 0
    target = 'ff' if difficulty == 2 else 'ffff'
    
    message =sender+recipient+subject+body+str(non)
    
    while calculate_hash(message)[:len(target)] != target:
        non += 1
        attempts += 1
        message =sender+recipient+subject+body+str(non)
    
    return non, attempts

sender_email = "xyz@xample.com"
recipient_email = "abc@example.com"
email_subject = "Hello"
message_body = "This is the message body"
nonce_1 = 0
difficulty_1 = 2

nonce_result_1, attempts_1 = All_Data(sender_email, recipient_email, email_subject, message_body, nonce_1, difficulty_1)
print(f"Task 1: Nonce found: {nonce_result_1}")
print(f"Task 1: Attempts taken: {attempts_1}")

nonce_2 = nonce_result_1
difficulty_2 = 4

nonce_result_2, attempts_2 = All_Data(sender_email, recipient_email, email_subject, message_body, nonce_2, difficulty_2)
print(f"Task 2: Nonce found: {nonce_result_2}")
print(f"Task 2: Attempts taken: {attempts_2}")
