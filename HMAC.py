import hashlib
import hmac

def sign(message, key):
    # Sign the message using HMAC and the specified key
    signature = hmac.new(key, message.encode(), hashlib.sha256).hexdigest()
    return signature

def verify(message, key, signature):
    # Sign the message using the same key
    expected_signature = sign(message, key)

    # Check if the signature matches the expected signature
    return hmac.compare_digest(signature, expected_signature)

# Test the HMAC implementation

# Set the message and key
message = "This is the message to be signed. Kalpana Regmi"
key = b"Kalpana Regmi"

# Sign the message
signature = sign(message, key)
print("Signature:", signature)

# Verify the signature
result = verify(message, key, signature)
print("Verified:", result)

# Try to verify the signature with a different key
result = verify(message, b"wrong key", signature)
print("Verified with wrong key:",result)
