
from email.mime import application
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from numpy import True_
from sqlalchemy import false
import recommendation

app = Flask(__name__)
api = Api(app)



class App_res(Resource):
    def get(self):
        query = request.args.get('q1')
        if query is None:
            return {'error': 'Please enter URL q1 param'}, 400
        else:
            res = recommendation.results(query)
            return jsonify(res) 
 

api.add_resource(App_res, '/')
if __name__ == '__main__':
    app.run(host='192.168.8.113',port=3579,debug=True, use_reloader=False)







    # To change the port and run the application with new changes should use python app.py  command  n terminal   

    # host= ip_address of ur machine and to get it directly  write  ipconfig in cmd 

    








    # from flask import Flask, request
# from flask_restful import Resource, Api
# import recommendation

# app = Flask(__name__)
# api = Api(app)

# class HelloWorld(Resource):
#     def get(self):
#         res = recommendation.results(request.args.get('q1'))
#         return {'appRes': res}

# api.add_resource(HelloWorld, '/')

# if __name__ == '__main__':
#     app.run(debug=True,port=2527)