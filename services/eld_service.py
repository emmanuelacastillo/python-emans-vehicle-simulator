from flask import request


def start_eld_services(app):

    @app.route('/eld/vehicle/info', methods=['POST'])
    def display_vehicle_info():
        request_json = request.get_json()

    @app.route('/eld/vehicle/warning', methods=['POST'])
    def display_vehicle_info():
        request_json = request.get_json()

    @app.route('/eld/navigation/info', methods=['POST'])
    def display_vehicle_info():
        request_json = request.get_json()
