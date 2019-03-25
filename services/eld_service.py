from flask import Flask, request, Response

app = Flask(__name__)

HTTP_STATUS_OK: int = 200
HTTP_STATUS_ERROR: int = 400


def run_eld_services():

    def handle_data(data) -> Response:
        if data is None:
            return Response('', status=HTTP_STATUS_ERROR)
        print(data)
        return Response('', status=HTTP_STATUS_OK)

    @app.route('/eld/vehicle/info', methods=['POST'])
    def display_vehicle_info():
        print("\nVehicle General Received...")
        return handle_data(request.get_json())

    @app.route('/eld/vehicle/warning', methods=['POST'])
    def display_vehicle_warning():
        print("\nVehicle Warning Received...")
        return handle_data(request.get_json())

    @app.route('/eld/navigation/info', methods=['POST'])
    def display_gps_info():
        print("\nNavigation Data Received...")
        return handle_data(request.get_json())

    app.run(host='0.0.0.0')
