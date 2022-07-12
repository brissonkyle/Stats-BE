# USER ENDPOINTS
from helpers.db_helpers import run_query
from app import Flask, request, Response, jsonify, json, app

@app.get('/api/user')
def user_get():
    user_data = run_query('SELECT username,email,password,bannerUrl,profileUrl FROM user')
    resp = []
    for data in user_data:
        userObj = {}
        userObj['username'] = data[0]
        userObj['email'] = data[1]
        userObj['password'] = data[2]
        userObj['bannerUrl'] = data[3]
        userObj['profileUrl'] = data[4]
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
    pass

@app.delete('/api/user')
def user_delete():
    pass