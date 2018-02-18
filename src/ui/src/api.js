import axios from 'axios'
let BASE;

if (process.env.NODE_ENV === 'development') {
  BASE = 'http://<IP>:<port>/api';
} else {
  BASE = '/api'
}

const fetch = (opts) => {
  return axios({
    headers: [
      {'Access-Control-Allow-Origin': '*'},
      {'Access-Control-Allow-Methods': 'GET, POST, PATCH, PUT, DELETE, OPTIONS' }
    ],
    method: opts.method || 'GET',
    url: opts.endpoint,
    baseURL: opts.baseURL || BASE,
    data: opts.data
  });
}

const createURL = (name) => {
  return(`/${name.replace(' ', '/')}`)
}

export { fetch, createURL }
