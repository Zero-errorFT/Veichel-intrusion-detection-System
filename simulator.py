import random

def generate_normal_data():
    return {
        "speed": random.randint(40, 90),
        "engine_temp": random.randint(85, 100),
        "rpm": random.randint(1800, 3200)
    }

def generate_attack_data():
    return {
        "speed": random.randint(180, 240),
        "engine_temp": random.randint(120, 160),
        "rpm": random.randint(5000, 7000)
    }

def generate_vehicle_data():

    # 20% chance of cyber attack
    if random.random() < 0.2:
        data = generate_attack_data()
        data["attack"] = True
    else:
        data = generate_normal_data()
        data["attack"] = False

    return data