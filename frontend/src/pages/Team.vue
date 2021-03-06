<template>
  <q-page class="column" padding>
    <div class="q-gutter-md row items-center">
      <q-select v-model="formation.selected" filled :options="formation.options" label="Formation" :style="{ width: '200px' }">
        <template v-slot:before>
          <q-icon name="mdi-soccer-field" />
        </template>
      </q-select>
      <q-input v-model="budget" filled label="Budget" mask="#, ###, ###, ###"
        fill-mask=""
        reverse-fill-mask
        input-class="text-right" :style="{ width: '200px' }">
        <template v-slot:before>
          <q-icon name="mdi-currency-eur" />
        </template>
      </q-input>
      <q-toggle v-model="include_free_agents" label="Include Free Agents" />
      <q-btn color="positive" label="Build" icon="mdi-hammer-screwdriver" @click="build()" />
    </div>
    <div class="q-ma-xs vertically-expanding fill-height-or-more">
      <tactics-board v-if="playerList.success" :squad="playerList.success" />
      <div class="vertically-expanding fill-height-or-more">
        <div class="q-gutter-md column">
          <div v-if="playerList.success" class="q-gutter-md">
            <q-list class="full-width" separator v-ripple >
              <q-item class="row items-center text-center bg-grey-3 text-bold">
                <q-section class="col">
                  <q-icon name="mdi-soccer"/> Position
                </q-section>
                <q-section class="col">
                  <q-icon name="mdi-format-text-variant-outline"/> Name
                </q-section>
                <q-section class="col">
                  <q-icon name="mdi-flag"/> Nationality
                </q-section>
                <q-section class="col">
                  <q-icon name="mdi-glasses"/> Age
                </q-section>
                <q-section class="col">
                  <q-icon name="mdi-security"/> Club
                </q-section>
                <q-section class="col">
                  <q-icon name="star"/> Overall
                </q-section>
                <q-section class="col text-right">
                  <q-icon name="mdi-currency-eur"/> Value
                </q-section>
              </q-item>
              <q-item class="text-center" v-for="(item, index) in playerList.success.formation" :key="index">
                <q-item-section>
                  {{ item.toUpperCase() }}
                </q-item-section>
                <q-item-section avatar>
                  <q-avatar>
                    <img alt="" :src="`${baseUrl}${playerList.success.results[item].photo}`" />
                  </q-avatar>
                </q-item-section>
                <q-item-section>
                  {{ playerList.success.results[item].name }}
                </q-item-section>
                <q-item-section>
                  {{ playerList.success.results[item].nationality }}
                </q-item-section>
                <q-item-section>
                  {{ playerList.success.results[item].age }}
                </q-item-section>
                <q-item-section>
                  {{ playerList.success.results[item].club }}
                </q-item-section>
                <q-item-section>
                  <span>
                    <q-icon name="star" /> {{ formatMoney(playerList.success.results[item].overall) }}
                  </span>
                </q-item-section>
                <q-item-section class="text-right">
                  <span>
                    <q-icon name="mdi-currency-eur" /> {{ formatMoney(playerList.success.results[item].value) }}
                  </span>
                </q-item-section>
              </q-item>
            </q-list>
            <div class="flex flex-center">
              <q-chip square color="green-10" text-color="white" icon="star">
                Overall: {{ playerList.success.total_overall }}
              </q-chip>
              <q-chip square color="orange-10" text-color="white" icon="mdi-currency-eur">
                Value: {{ formatMoney(playerList.success.total_value) }}
              </q-chip>
            </div>
          </div>
          <div v-else-if="playerList.error" class="flex flex-center vertically-expanding">
            <q-card class="bg-red-13 text-white"
            >
              <q-card-section>
                <div class="text-h6"><q-icon name="warning" /> Error</div>
              </q-card-section>
              <q-card-section class="q-pt-none">
                Ooops! Something went wrong!
              </q-card-section>
            </q-card>
          </div>
          <div v-else-if="playerList.loading" class="flex flex-center vertically-expanding">
            <q-card class="bg-secondary text-white">
              <q-card-section class="">
                <span class="text-strong">
                  <q-spinner
                    color="primary"
                    size="3em"
                    :thickness="3"
                  /> Loading...
                </span>
              </q-card-section>
            </q-card>
          </div>
          <div v-else class="flex flex-center vertically-expanding">
            <q-card class="bg-info text-black">
              <q-card-section>
                <div class="text-h6"><q-icon name="info" /> Info</div>
              </q-card-section>
              <q-card-section class="q-pt-none">
                <q-icon name="mdi-arrow-up" /> Please click build button to create a team.
              </q-card-section>
            </q-card>
          </div>
        </div>
      </div>
    </div>
  </q-page>
</template>

<script>
import { createNamespacedHelpers } from 'vuex'
import { isString } from 'lodash'
import { baseURL } from '../services/http'

import TacticsBoard from '../components/TacticsBoard'

const { mapState, mapActions } = createNamespacedHelpers('player')

// COLS_POS = [
//  'ls', 'st', 'rs',
//  'lf', 'cf', 'rf',
//  'lw', 'lam', 'cam', 'ram', 'rw',
//  'lm', 'lcm', 'cm', 'rcm', 'rm',
//  'lwb', 'ldm', 'cdm', 'rdm', 'rwb',
//  'lb', 'lcb', 'cb', 'rcb', 'rb', 'gk']
export default {
  name: 'Team',
  components: {
    TacticsBoard
  },
  data () {
    return {
      baseUrl: baseURL,
      formation: {
        options: [
          { label: '4-4-2', value: ['gk', 'rb', 'rcb', 'lcb', 'lb', 'rm', 'rcm', 'lcm', 'lm', 'rs', 'ls'] },
          { label: '4-1-2-1-2', value: ['gk', 'rb', 'rcb', 'lcb', 'lb', 'cdm', 'rcm', 'lcm', 'cam', 'rs', 'ls'] },
          { label: '4-2-4', value: ['gk', 'rb', 'rcb', 'lcb', 'lb', 'rw', 'rcm', 'lcm', 'lw', 'rs', 'ls'] },
          { label: '4-2-3-1', value: ['gk', 'rb', 'rcb', 'lcb', 'lb', 'rw', 'rcm', 'lcm', 'lw', 'cam', 'st'] },
          { label: '3-5-2', value: ['gk', 'rcb', 'cb', 'lcb', 'rm', 'rcm', 'cm', 'lcm', 'lm', 'rs', 'ls'] },
          { label: '5-3-2', value: ['gk', 'rcb', 'cb', 'lcb', 'rwb', 'lwb', 'rcm', 'lcm', 'cam', 'rs', 'ls'] }
        ],
        selected: { label: '4-4-2', value: ['gk', 'rb', 'rcb', 'lcb', 'lb', 'rm', 'rcm', 'lcm', 'lm', 'rs', 'ls'] }
      },
      budget: 1000000,
      include_free_agents: false
    }
  },
  computed: {
    ...mapState({
      playerList: state => state.list
    })
  },
  methods: {
    ...mapActions({
      buildTeam: 'buildTeam',
      resetList: 'resetList'
    }),
    build () {
      const regex = /,|_| /gi
      const budget = isString(this.budget) ? parseInt(this.budget.replace(regex, '')) : this.budget
      this.buildTeam({
        formation: this.formation.selected.value,
        budget,
        include_free_agents: this.include_free_agents
      })
    },
    formatMoney (amount) {
      return amount.toString().replace(/(\d)(?=(\d{3})+(?!\d))/g, '$1,')
    }
  },
  created () {
    this.resetList()
  }
}
</script>

<style lang="scss">
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
  flex-wrap: wrap;
  > div {
    flex: 1;
    display: flex;
  }
}

@media screen and (max-width: 900px) {
  .board {
    display: none !important;
  }
}
</style>
