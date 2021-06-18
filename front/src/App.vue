<template>
  <div id="app">
    <section class="dashboard">
      <div class="dashboard__row">
        <grafico-transacoes style="flex:2" :entries="transacoes" />
        <grafico-categoria-transacoes  :entries="transacoes" />
        
      </div>
      <div class="dashboard__row">
        <tabela-transacoes id="td-grid" :entries="transacoes" />
      </div>

    </section>
  </div>
</template>

<script>
import transacoes from './data/transacoes_teste.js';

import GraficoTransacoes from './components/GraficoTransacoes.vue';
import GraficoCategoriaTransacoes from './components/GraficoCategoriaTransacoes.vue';
import TabelaTransacoes from './components/TabelaTransacoes.vue';

export default {
  name: 'app',
  components: {

    GraficoTransacoes,
    GraficoCategoriaTransacoes,
    TabelaTransacoes,
  },
  data() {
    return {
      transacoes,
    }
  },
  mounted() {
  }
}
</script>
