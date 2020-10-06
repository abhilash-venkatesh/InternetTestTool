import os
import subprocess


class Ping:
    host = ""
    response_text = ""
    response = {}

    def __init__(self, host):
        self.host = host
        try:
            self.response_text = subprocess.check_output('ping -n 1 ' + host, shell=True).decode('utf-8')
        except subprocess.CalledProcessError as e:
            self.response_text = "No Internet"
        # print(self.response_text)
        self.parse_response()

    def get_response(self):
        return self.response

    def parse_response(self):
        all_response_lines = self.response_text.split('\n')
        if 'Reply from ' + self.host not in self.response_text:
            self.response['is_successful'] = False
            if 'Destination host unreachable' in self.response_text:
                self.response['details'] = 'Destination host unreachable'
        else:
            ping_response_line = all_response_lines[2]
            if 'Reply from ' + self.host in ping_response_line:
                self.response['is_successful'] = True
                self.response['details'] = {}
                self.response['details']['response_time'] = ping_response_line.split()[4].split('=')[1]
                self.response['details']['ttl'] = ping_response_line.split()[5].split('=')[1]
            # print(self.response)
