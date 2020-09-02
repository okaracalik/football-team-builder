<template>
  <q-page class="column" padding>
    <div class="q-gutter-md row items start">
      <q-select v-model="formation.selected" filled :options="formation.options" label="Formation" :style="{ width: '200px' }">
        <template v-slot:before>
          <q-icon name="mdi-soccer-field" />
        </template>
      </q-select>
      <q-input v-model="formation.budget" filled label="Budget" :style="{ width: '300px' }">
        <template v-slot:before>
          <q-icon name="mdi-currency-eur" />
        </template>
      </q-input>
    </div>
    <div class="q-ma-xs bg-red-2 vertically-expanding fill-height-or-more">
      <div class="bg-cyan-2"></div>
      <div class="bg-yellow-2">
        <q-list separator >
          <q-item v-for="(item, index) in formation.selected.value" :key="index">
            <q-item-section>
              {{ item }}
            </q-item-section>
          </q-item>
        </q-list>
      </div>
    </div>
  </q-page>
</template>

<script>
export default {
  name: 'Team',
  data () {
    return {
      formation: {
        options: [
          { label: '4-4-2', value: ['GK', 'RB', 'RCB', 'LCB', 'LB', 'RM', 'RCM', 'LCM', 'ML', 'RCF', 'LCF'] },
          { label: '4-1-2-1-2', value: ['GK', 'RB', 'RCB', 'LCB', 'LB', 'CDM', 'RCM', 'LCM', 'CAM', 'RCF', 'LCF'] },
          { label: '4-2-4', value: ['GK', 'RB', 'RCB', 'LCB', 'LB', 'RAM', 'RCM', 'LCM', 'LAM', 'RCF', 'LCF'] },
          { label: '4-2-3-1', value: ['GK', 'RB', 'RCB', 'LCB', 'LB', 'RAM', 'RCM', 'LCM', 'LAM', 'CAM', 'CF'] },
          { label: '3-5-2', value: ['GK', 'RCB', 'DC', 'LCB', 'RM', 'RCM', 'MC', 'LCM', 'ML', 'RCF', 'LCF'] },
          { label: '5-3-2', value: ['GK', 'RCB', 'DC', 'LCB', 'WBR', 'WBL', 'RCM', 'LCM', 'CAM', 'RCF', 'LCF'] }
        ],
        selected: { label: '4-4-2', value: ['GK', 'RB', 'RCB', 'LCB', 'LB', 'RM', 'RCM', 'LCM', 'ML', 'RCF', 'LCF'] }
      }
    }
  }
}
</script>

<style lang="scss">
.area {
  width: 100px;
  height: 100px;
  position: relative;
}

.layer {
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0;
  left: 0;
}

.top-layer {
  z-index: 10;
}

.tactics-board {
  display: grid;
  grid-template-columns: 20% 60% 20%;
  grid-template-rows: repeat(6, 1fr);
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  background-color: cornsilk;
}

.tactics-board > .column > .col, .tactics-board > .row > .col {
  border: 1px solid springgreen;
}

.squad-board {
  background-color: rgb(214, 192, 183);
  border: 2px solid tomato;
}

.vertically-expanding {
  display: flex;
  flex-direction: column;
  flex: 1;
  height: 100%;
}

.horizontally-expanding {
  flex: 1 1 auto;
}

.fill-height-or-more {
  min-height: 100%;
  display: flex;
  flex-direction: row;
  > div {
    flex: 1;
    display: flex;
  }
}
</style>
