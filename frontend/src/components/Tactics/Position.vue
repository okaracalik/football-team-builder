<template>
  <div class="position wrap">
    <span>
      <q-badge class="text-subtitle1" color="yellow-3" text-color="black" >{{player.name}}</q-badge>
    </span>
  </div>
</template>

<script>
export default {
  name: 'Position',
  props: {
    player: {
      type: Object,
      default: null
    }
  },
  data () {
    return {}
  }
}
</script>
