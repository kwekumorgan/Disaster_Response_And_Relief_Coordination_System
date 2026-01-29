import random

def get_disaster_state():
    disasters = ["None", "Flood", "Earthquake", "Fire"]
    severity = random.randint(1, 5)   # 1 = low, 5 = severe

    return {
        "disaster_type": random.choice(disasters),
        "severity_level": severity
    }
