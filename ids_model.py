import pandas as pd
from sklearn.ensemble import IsolationForest

# Normal driving dataset
training_data = pd.DataFrame({
    "speed":[40,45,50,55,60,65,70,75,80],
    "engine_temp":[88,89,90,91,92,90,89,91,90],
    "rpm":[2000,2100,2200,2300,2400,2500,2600,2700,2800]
})

model = IsolationForest(contamination=0.1)
model.fit(training_data)

def detect_intrusion(data):

    df = pd.DataFrame([{
        "speed":data["speed"],
        "engine_temp":data["engine_temp"],
        "rpm":data["rpm"]
    }])

    prediction = model.predict(df)

    if prediction[0] == -1:
        return True
    else:
        return False