import joblib
import numpy as np

__model = None

def get_estimated_price(sqft, landsqft, neighbors, stories, pool, bedrooms, bathrooms):
    with open("./server/artifacts/house_price_model.pkl", "rb") as f:
        global __model
        __model = joblib.load(f)

        x = np.array([sqft, landsqft, neighbors, stories, pool, bedrooms, bathrooms])

    return round(__model.predict([x])[0], 2)

print(get_estimated_price(2000, 5000, 10, 2, 1, 3, 2))