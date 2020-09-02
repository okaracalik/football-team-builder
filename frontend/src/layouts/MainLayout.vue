<template>
  <q-layout view="lHh Lpr lFf">
    <q-header class="bg-green-13 text-grey-10" elevated>
      <q-toolbar >
        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="leftDrawerOpen = !leftDrawerOpen"
        />

        <q-toolbar-title>
          Football Team Builder
        </q-toolbar-title>

      </q-toolbar>
    </q-header>

    <q-drawer v-model="leftDrawerOpen" show-if-above bordered content-class="bg-grey-1">
      <q-list>
        <q-item-label header class="text-grey-8">Menu</q-item-label>
        <q-item clickable tag="a" to="/search">
          <q-item-section avatar>
            <q-icon name="mdi-badge-account-horizontal" />
          </q-item-section>
          <q-item-section>
            <q-item-label>Search Players</q-item-label>
          </q-item-section>
        </q-item>
        <q-item clickable tag="a" to="/team">
          <q-item-section avatar>
            <q-icon class="rotate-90" name="mdi-soccer-field" />
          </q-item-section>
          <q-item-section>
            <q-item-label>Build a Team</q-item-label>
          </q-item-section>
        </q-item>
      </q-list>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>

export default {
  name: 'MainLayout',

  data () {
    return {
      leftDrawerOpen: false
    }
  }
}
</script>
