<script setup lang="ts">
import UIContainerVue from "./UIContainer.vue";
</script>

<template>
  <header class="header">
    <UIContainerVue>
      <div class="header__container">
        <h1 class="header__logo">My Animes</h1>
        <nav class="nav">
          <ul class="nav__list">
            <li class="nav__item">
              <router-link v-bind:to="''" class="nav__link"
                >Iniciar sessión</router-link
              >
            </li>
          </ul>
        </nav>
      </div>
    </UIContainerVue>
  </header>
</template>

<style>
.header {
  background-color: var(--bg-secondary);
}

.header__container {
  display: flex;
  justify-content: space-between;
}

.nav__list {
  list-style: none;
  margin: 0;
  padding: 0;
}

.nav__item {
  height: 100%;
  display: flex;
  align-items: center;
  text-align: center;
}

.nav__link {
  padding: 15px;
}
</style>
