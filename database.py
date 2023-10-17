import sqlalchemy, os, json
from sqlalchemy import create_engine, text

connectionstring = os.environ['CString']
engine = create_engine(connectionstring,
                       connect_args={"ssl": {
                           "ssl-ca": "/etc/ssl/cert.pem"
                       }})


def get_user_details():
  with engine.connect() as conn:
    # Construct a SQL query to select all data from a table
    query = text("SELECT * FROM quotations")
    result = conn.execute(query)

    # Fetch all rows from the result
    rows = result.fetchall()

    # Create a list to store dictionaries for each row
    rows_as_dicts = []

    # Get the column names from the result object
    column_names = result.keys()

    # Iterate through the rows and convert each to a dictionary
    for row in rows:
      row_dict = {}
      for i, column_name in enumerate(column_names):
        row_dict[column_name] = row[i]
      rows_as_dicts.append(row_dict)

  # Serialize the list of dictionaries to JSON

  json_data = json.dumps(rows_as_dicts)

  # Print or do whatever you need with the JSON data
  return json_data


def insert_data(data):
  with engine.connect() as conn:
    # Prepare the SQL query
    query = text(
        f"INSERT INTO quotations (name, mail,tel,movingdate,orign,destination,specreq) VALUES ('{data['name']}', '{data['email']}','{data['phone']}','{data['moving_date']}','{data['origin']}','{data['destination']}','{data['special_requests']}')"
    )
    # Execute the query and insert the data
    conn.execute(query)


def insert_data_details(cdata):
  with engine.connect() as conn:
    # Prepare the SQL query
    query = text(
        f"INSERT INTO contactform (name,mail,message) VALUES ('{cdata['cname']}', '{cdata['cemail']}','{cdata['cmessage']}')"
    )
    # Execute the query and insert the data
    conn.execute(query)
