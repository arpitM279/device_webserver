# python3

import uuid
import datetime
from flask import Flask


from postgres_utils import PostgresUtils
from config import config

app = Flask(__name__)

DEVICE_TABLE_STR = """
        CREATE TABLE devices (
            unique_id SERIAL PRIMARY KEY,
            device_name VARCHAR(255) NOT NULL
        )
        """

def get_curent_datetime():
    return datetime.datetime.now().strftime("%Y-%b-%d %H:%M:%S")

@app.route("/add-device/<device_name>", methods = ["POST"])
def add_device(device_name):
    device_unique_identifier = "device" + "_" + str(uuid.uuid4())
    temp_sensor_unique_identifier = "ts" + "_" +  str(uuid.uuid4())
    pressure_sensor_unique_identifier = "ps" + "_" + str(uuid.uuid4())
    
    # create devices table if not created 
    

    return device_name + "-" + device_unique_identifier + "\n"

def main():
    conf = config()
    print(conf)
    db_conn = PostgresUtils()
    db_conn.connect(conf)
    db_conn.execute_command(DEVICE_TABLE_STR)

    # app.run(host="0.0.0.0", port=5050, debug=True)
    # print (get_curent_datetime())


if __name__ == '__main__':
    main()
