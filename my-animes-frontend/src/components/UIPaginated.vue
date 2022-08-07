<script setup lang="ts">
import { ref } from "vue";

const props = defineProps<{
  currentPage: number;
  totalPages: number;
  formatterURL: (page: number) => string;
}>();

const pages = ref<string[]>();
pages.value = Array(props.totalPages).map((v) => props.formatterURL(v));
</script>

<template>
  <div>
    <a v-for="page in pages" :href="page"></a>
  </div>
</template>
