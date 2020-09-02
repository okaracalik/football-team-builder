export const listSuccess = (state, payload) => {
  state.list.success = payload
}

export const listError = (state, payload) => {
  state.list.error = payload
}

export const itemSuccess = (state, payload) => {
  state.item.success = payload
}

export const itemError = (state, payload) => {
  state.item.error = payload
}
