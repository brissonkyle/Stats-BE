# USER ENDPOINTS
from helpers.db_helpers import run_query
from app import Flask, request, Response, jsonify, json, app

def grabId(email,password):
    result = run_query('SELECT id FROM user WHERE email=? AND password=?',[email,password])
    if result == []:
        return None
    user_id = result[0][0]
    return user_id

@app.get('/api/user')
def user_get():
    user_data = run_query('SELECT username,bannerUrl,profileUrl FROM user')
    resp = []
    for data in user_data:
        userObj = {}
        userObj['username'] = data[0]
        userObj['bannerUrl'] = data[1]
        userObj['profileUrl'] = data[2]
        resp.append(userObj)
    return jsonify(resp), 200

@app.post('/api/user')
def user_post():
    user_resp = request.json
    username = user_resp.get('username')
    email = user_resp.get('email')
    password = user_resp.get('password')
    bannerUrl = user_resp.get('bannerUrl')
    profileUrl = user_resp.get('profileUrl')
    run_query('INSERT INTO user (username,email,password,bannerUrl,profileUrl) VALUES (?,?,?,?,?)', [username,email,password,bannerUrl,profileUrl])
    return jsonify('User Created !!'), 200

@app.patch('/api/user')
def user_patch():
    user_resp = request.json
    token = user_resp.get('token')
    password = user_resp.get('password')
    bannerUrl = user_resp.get('bannerUrl')
    profileUrl = user_resp.get('profileUrl')
    if token:
        run_query('UPDATE user SET password=?, bannerUrl=?, profileUrl=? WHERE token=?', [password,bannerUrl,profileUrl,token])
        return jsonify('User updated'), 201
    if not token:
        return jsonify('Must provide a valid session token'), 401

@app.delete('/api/user')
def user_delete():
    user_resp = request.json
    token = user_resp.get('token')
    email = user_resp.get('email')
    if token:
        run_query('DELETE FROM user WHERE email=?', [email])
        return jsonify('User Deleted'), 200
    if not token:
        return jsonify('Must provide a valid session token'), 401