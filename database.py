import sqlite3
import json

con = sqlite3.connect('./data/ireves.db', check_same_thread=False)
cur = con.cursor()


def get_all_regions():
    cur.execute('SELECT * FROM regions')
    row_headers = [x[0]
                   for x in cur.description]  # this will extract row headers
    return result_to_json(cur.fetchall(), row_headers)


def get_region_by_id(region_id):
    cur.execute('SELECT * FROM regions WHERE regions.id = :id',
                {"id": region_id})
    row_headers = [x[0]
                   for x in cur.description]  # this will extract row headers
    return result_to_json(cur.fetchall(), row_headers)


def get_region_pop(region_id):
    cur.execute('SELECT population FROM regions WHERE regions.id = :id', {
                "id": region_id})
    return cur.fetchone()[0]


def get_region_bounds(region_id):
    region_id = int(region_id)
    cur.execute('SELECT * FROM regions WHERE regions.id = :id', {
                "id": region_id})
    if  cur.fetchone() is None:
        return "Not found"
    else:
        boundsFile = open('./data/region_bounds/%i.json'%region_id)
        bounds = json.load(boundsFile)
        return bounds


def result_to_json(rv, row_headers):
    json_data = []
    for result in rv:
        json_data.append(dict(zip(row_headers, result)))
    return json.dumps(json_data)

