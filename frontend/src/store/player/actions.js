import HTTP, { baseURL } from '../../services/http'

const moduleName = 'players'
const Service = HTTP(moduleName)

export const resetList = ({ commit }) => {
  commit('listReset')
}

export const find = ({ commit }, query = null) => {
  commit('listReset')
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
  commit('listReset')
  commit('listLoading')
  Service.custom({ method: 'post', url: `${baseURL}/players/team`, data })
    .then(success => {
      commit('listSuccess', success.data)
    })
    .catch(err => {
      commit('listError', err.response)
    })
}
