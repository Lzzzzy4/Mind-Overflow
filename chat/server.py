# from model import chat_model
import threading
class chat_model:
  def query(self, question):
    ret = f"Nice query: {question}"
    return ret

  def direct_query(self, question):
    ret = f"Nice direct query: {question}"
    return ret

from flask import Flask, request, Request, Response, jsonify
app = Flask(__name__)

print("Loading model...")
mutex = threading.Lock()
model = chat_model()
print("Loaded!")

@app.route('/api/query', methods=['POST'])
def query():
  mutex.acquire()
  data = request.get_json()
  print("Received: ", data)
  res = { 'ans': model.query(data['text']) }
  print("Response: ", res)
  res = jsonify(res)
  mutex.release()
  return res

@app.route('/api/direct_query', methods=['POST'])
def direct_query():
  mutex.acquire()
  data = request.get_json()
  print("Received [DIRECT]: ", data)
  res = { 'ans': model.direct_query(data['text']) }
  print("Response: ", res)
  res = jsonify(res)
  mutex.release()
  return res
