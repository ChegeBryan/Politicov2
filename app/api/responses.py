from flask import jsonify, make_response


class Responses:
    """this class registers all my responses"""

    @staticmethod
    def complete_response(message):
        """this stores my response message"""
        response = make_response(jsonify({
            "Status": 200,
            "Data": message,
        }))
        return response

    @staticmethod
    def created_response(message):
        """this stores my response message"""
        response = make_response(jsonify({
            "Status": 201,
            "Data": message,
        }))
        return response

    @staticmethod
    def not_found(message):
        """this returns an invalid request message"""
        response = make_response(jsonify({
            "Status": 404,
            "Data": message
        }))
        return response

    @staticmethod
    def bad_request(message):
        response = make_response(jsonify({
            'Status': 400,
            'Data': message
        }))
        return response


class AuthResponses:
    """For authentication with token"""

    @staticmethod
    def create_user(message, token):
        response = jsonify({"status": "User Created",
                            "message": message,
                            "access_token": token})
        return make_response(response), 201

    @staticmethod
    def complete_request(message, token):
        response = jsonify({"status": "OK",
                            "message": message,
                            "access_token": token})
        return make_response(response), 200
