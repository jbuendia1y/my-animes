<script setup lang="ts">
defineProps<{
  image: string;
  slug: string;
  title: string;
}>();
</script>

<template>
  <router-link :to="`/animes/${slug}`" class="m-1 card anime">
    <div class="card-img-top card__image-box">
      <img class="card__image" :src="image" :alt="title" />
    </div>
    <h2 class="card-title card__title">{{ title }}</h2>
  </router-link>
</template>

<style>
.anime {
  display: inline-block;
  width: 300px;
}

.card {
  background-color: var(--bg-secondary);
}

.card__image {
  height: 100%;
  width: 100%;
  object-fit: cover;
  object-position: top;
}

.card__image-box {
  max-height: 325px;
}

.card__title {
  width: 100%;
  padding: 0.7rem 1rem;
}
</style>
