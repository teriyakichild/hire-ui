import requests
import sys
import json
class hireapi:
    url='http://hire-nytefyre.rhcloud.com/api/'
    def __init__(self):
      pass
    def _request(self,uri,method,payload=''):
      ret = {}
      try:
        if method == 'get':
          r = requests.get(self.url+uri);
        elif method == 'post':
          headers = {'content-type': 'application/json'}
          r = requests.post(self.url+uri, data=json.dumps(payload), headers=headers)
      except requests.exceptions.ConnectionError:
        sys.exit('Fatal Error:  Connection to '+self.url+' unsuccessful')
      except Exception, e:
        print str(e)
      if r.status_code != 200:
        ret['status'] = 'error'
        ret['message'] = 'Status Code: '+str(r.status_code)
      else:
        ret['status'] = 'success'
      ret['data'] = r.text
      return ret
    def _get(self,uri):
      return self._request(uri,'get')
    def _post(self,uri,payload):
      return self._request(uri,'post',payload)
    def list_users(self):
      ret = self._get('user')
      return ret
    def list_candidates(self):
      ret = self._get('candidate')
      return ret
    def list_panels(self,userid):
      ret = self._get('panelist?q={"filters": [{"name": "userid", "val": "' + userid + '", "op": "eq"}]}')
      return ret
    def search_users(self,query):
      ret = self._get('user?q={"filters": [{"name": "name", "val": "%' + query + '%", "op": "like"}]}')
      return ret
    def new_user(self,name,password):
      payload = { 'name': name, 'password': password }
      ret = self._post('user',payload)
      return ret

if __name__ == "__main__":
    hireapi = hireapi()
    print hireapi.list_users()['data']
    print hireapi.list_candidates()['data']
    print hireapi.list_panels('3')['data']
    print hireapi.search_users('admin')
    print hireapi.new_user('Tony Rogers','testing123')['data']
