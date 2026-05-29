import validate

class Server:
    os_type = "Linux"

    def __init__(self, hostname, ip_address, max_connections=10, status="inactive"):
        self._hostname = validate.validate_hostname(hostname)
        self._ip_address = validate.validate_ip_address(ip_address)
        self._max_connections = validate.validate_max_connections(max_connections)
        self._status = validate.validate_status(status)
        self._current_connections = 0

    def __str__(self):
        return f"Server({self._hostname}, {self._ip_address}, {self._status})"

    def __repr__(self):
        return f"Server(hostname='{self._hostname}', ip='{self._ip_address}', max_conn={self._max_connections}, status='{self._status}')"

    def __eq__(self, other):
        if not isinstance(other, Server):
            return False
        return self._ip_address == other._ip_address

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = validate.validate_status(value)

    @property
    def max_connections(self):
        return self._max_connections

    @max_connections.setter
    def max_connections(self, value):
        self._max_connections = validate.validate_max_connections(value)

    @property
    def current_connections(self):
        return self._current_connections

    def activate(self):
        self._status = "active"

    def maintenance_mode(self):
        self._status = "maintenance"

    def connect_user(self, user):
        validate.validate_connections(self._current_connections + 1, self._max_connections)
        self._current_connections += 1

    def disconnect_user(self, user):
        if self._current_connections > 0:
            self._current_connections -= 1
