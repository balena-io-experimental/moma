import axios from 'axios'

const BASE = '/api';

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

export { fetch }
