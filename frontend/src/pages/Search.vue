<template>
  <q-page padding>
    <div class="q-gutter-md row items-center q-mb-md">
      <q-input v-model="search.name" filled type="search" label="Search by Name">
        <template v-slot:prepend>
          <q-icon name="mdi-format-text-variant" />
        </template>
      </q-input>
      <q-input v-model="search.club" filled type="search" label="Search by Club">
        <template v-slot:prepend>
          <q-icon name="mdi-tshirt-crew" />
        </template>
      </q-input>
      <q-input v-model="search.nationality" filled type="search" label="Search by Nationality">
        <template v-slot:prepend>
          <q-icon name="mdi-flag" />
        </template>
      </q-input>
      <q-btn color="teal" label="Search" icon="search" @click="onFilter()" />
      <q-btn color="warning" label="Reset" icon="mdi-refresh" @click="reset()" />
    </div>
    <!-- content -->
    <q-table
      v-if="playerList.success"
      dense
      :data="playerList.success.results"
      :columns="columns"
      :row-key="uniqueKey"
      :pagination.sync="pagination"
      @request="onRequest"
    >
      <template v-slot:body-cell-photo="props">
        <q-td :props="props">
          <q-img
            :src="`${baseUrl}${props.value}`"
          />
        </q-td>
      </template>
    </q-table>
    <div v-else-if="playerList.error" class="flex flex-center vertically-expanding">
        <q-card class="bg-red-13 text-white">
          <q-card-section>
            <div class="text-h6"><q-icon name="warning" /> Error</div>
          </q-card-section>
          <q-card-section class="q-pt-none">
            Ooops! Something went wrong!
          </q-card-section>
        </q-card>
      </div>
      <div v-else-if="playerList.loading" class="flex flex-center vertically-expanding">
        <q-card class="bg-teal-1 text-black">
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
            <q-icon name="mdi-arrow-top-left" /> Please click search button to see players.
          </q-card-section>
        </q-card>
      </div>
  </q-page>
</template>

<script>
import { createNamespacedHelpers } from 'vuex'
import { baseURL } from '../services/http'

const { mapState, mapActions } = createNamespacedHelpers('player')

export default {
  name: 'Search',
  mixins: [],
  props: {},
  data () {
    return {
      baseUrl: baseURL,
      search: {
        name: '',
        club: '',
        nationality: ''
      },
      pagination: {
        page: 1,
        rowsPerPage: 15,
        rowsNumber: 1
      },
      uniqueKey: 'id',
      columns: [
        { name: 'photo', field: 'photo', label: 'Photo', style: 'width: 50px' },
        { name: 'name', field: 'name', label: 'Name' },
        { name: 'club', field: 'club', label: 'Club' },
        { name: 'age', field: 'age', label: 'Age' },
        { name: 'nationality', field: 'nationality', label: 'Nationality' },
        { name: 'overall', field: 'overall', label: 'Overall' },
        { name: 'value', field: 'value', label: 'Value (€)', format: this.formatMoney }
      ]
    }
  },
  computed: {
    ...mapState({
      playerList: state => state.list
    })
  },
  methods: {
    ...mapActions({
      findPlayers: 'find'
    }),
    onRequest (props) {
      const name = this.search.name === '' ? null : this.search.name
      const club = this.search.club === '' ? null : this.search.club
      const nationality = this.search.nationality === '' ? null : this.search.nationality
      const { page, rowsPerPage } = props.pagination
      this.findPlayers({ params: { skip: (page - 1) * rowsPerPage, limit: rowsPerPage, name, club, nationality } })
      this.pagination.page = page
      this.pagination.rowsPerPage = rowsPerPage
    },
    onFilter () {
      const name = this.search.name === '' ? null : this.search.name
      const club = this.search.club === '' ? null : this.search.club
      const nationality = this.search.nationality === '' ? null : this.search.nationality
      const { page, rowsPerPage } = this.pagination
      this.findPlayers({ params: { skip: (page - 1) * rowsPerPage, limit: rowsPerPage, name, club, nationality } })
    },
    reset () {
      this.search = {
        name: '',
        club: '',
        nationality: ''
      }
      this.pagination = {
        page: 1,
        rowsPerPage: 15,
        rowsNumber: 1
      }
      this.onFilter()
    },
    formatMoney (amount) {
      return amount.toString().replace(/(\d)(?=(\d{3})+(?!\d))/g, '$1,')
    }
  },
  created () {
    this.onRequest({
      pagination: this.pagination
    })
  },
  watch: {
    'playerList.success' (newValue) {
      this.pagination.rowsNumber = newValue.count
    }
  }
}
</script>
