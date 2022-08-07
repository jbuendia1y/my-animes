<script setup lang="ts">
import { ref } from "vue";
import { Anime, getAnimes } from "../repositories/animes.repository";
import AnimeCard from "../components/AnimeCard.vue";
import { Page } from "../interfaces";
import UIPaginated from "../components/UIPaginated.vue";

const animes = ref<Page<Anime>>();

getAnimes().then((v) => {
  animes.value = v;
});

const formatterURL = (page: number) => {
  return `/animes/${page}`;
};
</script>
<template>
  <div class="container d-flex mt-2 home">
    <template v-if="animes">
      <AnimeCard
        v-for="anime of animes.data"
        :image="anime.image"
        :title="anime.title"
        :slug="anime.slug"
      />
      <UIPaginated
        :currentPage="animes.currentPage"
        :totalPages="animes.totalPages"
        :formatterURL="formatterURL"
      />
    </template>
    <div v-else>
      <span>Loading ...</span>
    </div>
  </div>
</template>

<style>
.home {
  flex-wrap: wrap;
  justify-content: center;
}
</style>
