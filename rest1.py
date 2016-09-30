def api_req_raw(self, method, path, body=None, **kwargs):
        for host in self.__hosts:
            path_str = os.path.join(host, 'v2')
            if len(path) == 2:
                assert(path[0] == 'apps')
                path_str += '/apps/{0}'.format(path[1])
            else:
                path_str += '/' + path[0]
            response = requests.request(
                method,
                path_str,
                headers={
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                **kwargs
            )
            if response.status_code == 200:
                break

        response.raise_for_status()
        return response
