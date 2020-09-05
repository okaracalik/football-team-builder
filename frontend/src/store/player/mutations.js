export const listLoading = (state) => {
  state.list.loading = true
}

export const listSuccess = (state, payload) => {
  state.list.loading = false
  state.list.success = payload
}

export const listError = (state, payload) => {
  state.list.loading = false
  state.list.error = payload
}

export const itemSuccess = (state, payload) => {
  state.item.success = payload
}

export const itemError = (state, payload) => {
  state.item.error = payload
}
