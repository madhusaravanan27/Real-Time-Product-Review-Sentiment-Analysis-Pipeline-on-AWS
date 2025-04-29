import boto3
import json
import time
import random

# Connect to Kinesis
kinesis = boto3.client('kinesis', region_name='us-east-1')

# Sample reviews
reviews = [
    "This product is amazing, I loved it!",
    "Terrible, completely broke after two days.",
    "Works okay, not too bad but not excellent.",
    "Exceeded my expectations, would buy again!",
    "Horrible service and cheap quality.",
    "Fantastic build quality, very sturdy and reliable.",
    "The product stopped working within a week, very disappointed.",
    "Highly recommend this to everyone!",
    "Not worth the price at all.",
    "Good value for money, happy with my purchase.",
    "Customer support was very helpful and quick to respond.",
    "Received a defective item, had to return it.",
    "Absolutely love it! Five stars!",
    "The size was smaller than expected.",
    "Color and design were exactly as shown.",
    "Battery life is terrible, needs frequent charging.",
    "Best investment I've made this year!",
    "It’s okay for occasional use but not for heavy usage.",
    "Poor packaging, item arrived damaged.",
    "Super fast shipping, arrived earlier than expected!",
    "The quality feels cheap and flimsy.",
    "User manual was confusing and hard to understand.",
    "Very easy to set up and use, even for beginners.",
    "Overheats after prolonged use, not recommended.",
    "Stylish design and lightweight, perfect for travel.",
    "Missing parts in the box, very frustrating experience.",
    "Works perfectly as advertised!",
    "Keeps crashing, very unstable product.",
    "Love the eco-friendly packaging and sustainability focus.",
    "Too noisy during operation, couldn't tolerate it.",
    "Affordable and does the job well enough.",
    "This product is amazing, I loved it!",
    "Terrible, broke after two days.",
    "Exceeded my expectations!",
    "Horrible service and cheap quality.",
    "Fantastic build quality, very reliable.",
    "Not worth the price.",
    "Customer support was excellent.",
    "It’s okay for the price.",
    "Battery life is terrible.",
    "Super fast shipping!",
    "Received a defective item.",
    "Love the sustainability focus.",
    "Too noisy, returned it.",
    "Very easy to set up.",
    "Stylish and lightweight."
]

while True:
    review = random.choice(reviews)
    data = {
        'review': review
    }
    print(f"Pushing review: {review}")
    kinesis.put_record(
        StreamName="review-stream",
        Data=json.dumps(data),
        PartitionKey="partitionkey"
    )
    time.sleep(10)  # Send 1 review every 10 seconds
