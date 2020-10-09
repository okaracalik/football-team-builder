<template>
  <div class="zone">
    <div v-if="$slots.left">
      <slot name="left"></slot>
    </div>
    <div v-if="$slots.center">
      <slot name="center"></slot>
    </div>
    <div v-if="$slots.right">
      <slot name="right"></slot>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Zone',
  data () {
    return {}
  }
}
</script>

<style lang="scss">
  .zone {
    display: flex;
    flex: 1;
    > div {
      display: flex;
      border-top: 1px solid tomato;
      border-right: 1px solid tomato;
    }
  }

  .zone > div:first-child {
    flex: 1
  }

  .zone > div {
    flex: 2
  }

  .zone > div:last-child {
    flex: 1
  }
</style>
