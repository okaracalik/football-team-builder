import HTTP, { base } from '../../services/http'

const moduleName = 'players'
const Service = HTTP(moduleName)

export const find = ({ commit }, query = null) => {
  commit('listLoading')
  Service.find(query)
    .then(success => {
      commit('listSuccess', success.data)
    })
    .catch(err => {
      commit('listError', err.response.data)
    })
}

export const get = ({ commit }, id) => {
  Service.get(id)
    .then(success => {
      commit('itemSuccess', { ...success.data })
    })
    .catch(err => {
      commit('itemError', err.response.data)
    })
}

export const buildTeam = ({ commit }, data) => {
  Service.custom({ method: 'post', url: `${base}/players/team`, data })
    .then(success => {
      commit('listSuccess', success.data)
    })
    .catch(err => {
      commit('listError', err.response)
    })
}
