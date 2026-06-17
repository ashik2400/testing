# raw_tokens = ["The", "AI", "model", "is", "LEARNING", "to", "see", "PATTERNS"]

# my_list = [i.lower() for i in raw_tokens if len(i) > 3 ]
# print(my_list)


# classes = ["negative", "neutral", "positive"]

# cls_labels = {cls: idx for idx ,cls in enumerate(classes)}

# print(cls_labels)

# predictions = {"car": 0.953, "truck": 0.421, "pedestrian": 0.887, "bicycle": 0.152}
# crcted = {label: round(score, 1) 
#           for label, score in predictions.items() 
#           if score > 0.80}

# print(crcted)
# sequence_tags = ["<PAD>", "<B-LOC>", "<O>", "<I-LOC>", "<PAD>", "<B-ORG>", "<O>"]
# remove_values = ["<PAD>","<O>"]
# crcted = (i for i in sequence_tags if i not in remove_values) 
# print(crcted)