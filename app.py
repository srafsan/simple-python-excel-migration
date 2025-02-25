from flask import Flask, jsonify
import pandas as pd
from flask_cors import CORS
from sqlalchemy import create_engine

app = Flask(__name__)
CORS(app)

host = "localhost"
user = "root"
password = ""
database = "python_data_migration"
table = "users"

# Database connection
engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{database}")

@app.route("/users", methods=["GET"])
def get_users():
    query = "SELECT * FROM users"
    df = pd.read_sql(query, con=engine)
    return jsonify(df.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True)
