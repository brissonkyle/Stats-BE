# USER LOGIN ENDPOINTS

from app import app, Flask, request, Response, json, jsonify
from helpers.db_helpers import run_query
import uuid

def grabId(email,password):
    result = run_query('SELECT id FROM user WHERE email=? AND password=?',[email,password])
    if result == []:
        return None
    user_id = result[0][0]
    return user_id

@app.post('/api/user-login')
def user_login():
    user_resp = request.json
    email = user_resp.get('email')
    password = user_resp.get('password')
    token = uuid.uuid4().hex
    user_id = grabId(email,password)
    if user_id == None:
        return('Invalid Email and Password'), 401
    run_query('INSERT INTO user_session (token,user_id) VALUES (?,?)', [token,user_id])
    return jsonify(token,user_id), 201

@app.delete('/api/user-login')
def user_logout():
    user_resp = request.json
    token = user_resp.get('token')
    if token:
        run_query('DELETE FROM user_session WHERE token=?', [token])
        return jsonify('You logged out'), 204
    if not token:
        return jsonify('Must provide a valid session token'), 401

