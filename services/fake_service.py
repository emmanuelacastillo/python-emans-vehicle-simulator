from flask import request


def start_fake_data_services(app):

    @app.route('/fake/data/vehicleinfo', methods=['GET'])
    def display_vehicle_info():
        request_json = request.get_json()

    @app.route('/fake/data/locationinfo', methods=['GET'])
    def display_vehicle_info():
        request_json = request.get_json()

    @app.route('/eld/navigation/info', methods=['GET'])
    def display_vehicle_info():
        request_json = request.get_json()
