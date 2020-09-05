import axios from 'axios'

const dev = 'http://localhost:3033'
const prod = 'https://localhost/api/football-team-builder'
// const base = 'https://orkutkaracalik.info/api/football-team-builder'

export const baseURL = process.env.DEV ? dev : prod

const Service = name => ({
  find (query = null) {
    return axios.get(`${baseURL}/${name}`, { ...query })
  },
  get (id) {
    return axios.get(`${baseURL}/${name}/${id}`)
  },
  create (data) {
    return axios.post(`${baseURL}/${name}`, data)
  },
  update (id, data) {
    return axios.put(`${baseURL}/${name}/${id}`, data)
  },
  remove (id) {
    return axios.delete(`${baseURL}/${name}/${id}`)
  },
  custom (options) {
    return axios(options)
  }
})

export default Service
