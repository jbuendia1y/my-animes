<script lang="ts">
import { useRoute } from "vue-router";
import { Anime, getAnime } from "../repositories/animes.repository";
import { ref } from "vue";

export default {
  async setup() {
    const route = useRoute();
    const slug = route.params.slug as string;

    const anime = ref<Anime | null | undefined>(null);
    const error = ref<any>(null);

    anime.value = await getAnime(slug);
  },
};
</script>

<template></template>
