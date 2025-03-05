import http from 'k6/http';
export default function() {
  http.get('http://192.168.56.201');
}
