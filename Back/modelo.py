import pandas as pd
import json
from sklearn.cluster import KMeans
from row import Row
class KMeansModel:
    def predict(self, customers: str):
        data  = json.loads(customers)
        df = pd.DataFrame(data)
        X = df.iloc[: , [3,4]]
        print(f"X Shape {X.shape}")
        X.head()
        final_model = KMeans(n_clusters=5 , random_state= 42)
        final_model.fit(X)
        labels = final_model.labels_
        datareturn = []
        for i in range(df['annualIncome'].shape[0]):
            row = Row(int(df['annualIncome'][i]), int(df['score'][i]), int(labels[i]))
            datareturn.append(row)

        jsonStr = json.dumps([obj.__dict__ for obj in datareturn])
        return jsonStr