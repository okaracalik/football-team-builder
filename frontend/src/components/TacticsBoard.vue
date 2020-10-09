<template>
  <div class="relative-position bg-grey-6 board">
    <pitch class="layer full-width" />
    <div class="layer top-layer transparent tactics-board">
      <!-- striker -->
      <section class="pitch-zone">
        <div></div>
        <div>
          <Position v-if="getPlayer('ls')" :player="getPlayer('ls')"/>
          <Position v-if="getPlayer('st')" :player="getPlayer('st')"/>
          <Position v-if="getPlayer('rs')" :player="getPlayer('rs')"/>
        </div>
        <div></div>
      </section>
      <!-- attacking-midfield -->
      <section class="pitch-zone">
        <div>
          <Position v-if="getPlayer('lw')" :player="getPlayer('lw')"/>
        </div>
        <div>
          <Position v-if="getPlayer('lam')" :player="getPlayer('lam')"/>
          <Position v-if="getPlayer('cam')" :player="getPlayer('cam')"/>
          <Position v-if="getPlayer('ram')" :player="getPlayer('ram')"/>
        </div>
        <div>
          <Position v-if="getPlayer('rw')" :player="getPlayer('rw')"/>
        </div>
      </section>
      <!-- midfield -->
      <section class="pitch-zone">
        <div>
          <Position v-if="getPlayer('lm')" :player="getPlayer('lm')"/>
        </div>
        <div>
          <Position v-if="getPlayer('lcm')" :player="getPlayer('lcm')"/>
          <Position v-if="getPlayer('cm')" :player="getPlayer('cm')"/>
          <Position v-if="getPlayer('rcm')" :player="getPlayer('rcm')"/>
        </div>
        <div>
          <Position v-if="getPlayer('rm')" :player="getPlayer('rm')"/>
        </div>
      </section>
      <!-- defensive-midfield -->
      <section class="pitch-zone">
        <div>
          <Position v-if="getPlayer('lwb')" :player="getPlayer('lwb')"/>
        </div>
        <div>
          <Position v-if="getPlayer('ldm')" :player="getPlayer('ldm')"/>
          <Position v-if="getPlayer('cdm')" :player="getPlayer('cdm')"/>
          <Position v-if="getPlayer('rdm')" :player="getPlayer('rdm')"/>
        </div>
        <div>
          <Position v-if="getPlayer('rwb')" :player="getPlayer('rwb')"/>
        </div>
      </section>
      <!-- defense -->
      <section class="pitch-zone">
        <div>
          <Position v-if="getPlayer('lb')" :player="getPlayer('lb')"/>
        </div>
        <div>
          <Position v-if="getPlayer('lcb')" :player="getPlayer('lcb')"/>
          <Position v-if="getPlayer('cb')" :player="getPlayer('cb')"/>
          <Position v-if="getPlayer('rcb')" :player="getPlayer('rcb')"/>
        </div>
        <div>
          <Position v-if="getPlayer('rb')" :player="getPlayer('rb')"/>
        </div>
      </section>
      <!-- goalkeeper -->
      <section class="pitch-zone">
        <div></div>
        <div class="goal">
          <Position v-if="getPlayer('sw')" :player="getPlayer('sw')"/>
          <Position v-if="getPlayer('gk')" :player="getPlayer('gk')"/>
        </div>
        <div></div>
      </section>
    </div>
  </div>
</template>

<script>
/* eslint-disable vue/no-unused-components */
import Pitch from './Tactics/Pitch'
import Position from './Tactics/Position'
import Zone from './Tactics/Zone'

export default {
  name: 'TacticsBoard',
  props: {
    squad: {
      type: Object,
      default: null
    }
  },
  components: {
    Pitch,
    Zone,
    Position
  },
  methods: {
    getPosition (position) {
      return this.squad.formation.includes(position)
    },
    getPlayer (position) {
      if (position in this.squad.results) {
        return this.squad.results[position]
      } else {
        return null
      }
    }
  }
}
</script>

<style lang="scss">
.layer {
  position: absolute;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
}

.top-layer {
  z-index: 10;
}

.board {
  padding: 6px;
  border-radius: 9px;
}

.tactics-board {
  display: flex;
  flex-direction: column;
  min-height: 100%;
  padding-top: 75px;
}

.pitch-zone {
  display: flex;
  flex: 1;
  & div {
    display: flex;
    &:first-child {
      flex: 1;
    }
    &:nth-child(2) {
      flex: 3;
    }
    &:last-child {
      flex: 1;
    }
    & .position {
        display: flex;
        align-items: center;
        justify-content: center;
      }
  }

  .goal {
    display: flex;
    flex-direction: column;
  }

}
</style>
