import HTTP from '../../services/http'

const moduleName = 'players'
const Service = HTTP(moduleName)

export const find = ({ commit }, query = null) => {
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
