<template>
  <div id="app">
    
    <div class = "container">
      <div class="logo-and-wordmark">
        <div class="logo">
          <img class="logo-img" :src="require('./assets/images/logo.png')"/>
        </div>
        <div class="wordmark">
          <span class="wordmark-text">MONI</span>
        </div>
      </div>    

      <barra v-bind:postURL="postURL"></barra>
 
      <section class="dashboard">
        <section class="dashboard__summary">
          <gasto-mensal :values="transacoes" :start="range.start" :end="range.end"/>
          <gasto-mensal :values="transacoes" :start="range.start" :end="range.end"/>
          <gasto-mensal :values="transacoes" :start="range.start" :end="range.end"/>
        </section>
        <br>
        <div class="dashboard__row">
          <grafico-transacoes style="flex:2" :entries="transacoes" />
          <grafico-categoria-transacoes  :entries="transacoes" />
        </div>
        <div class="dashboard__row">
          <tabela-transacoes id="td-grid" :entries="transacoes" />
        </div>
      </section>
      
    </div>

  </div>
</template>

<script>
import transacoes from './data/transacoes_teste.js';

import Barra from './components/Barra.vue'

import GraficoTransacoes from './components/GraficoTransacoes.vue';
import GraficoCategoriaTransacoes from './components/GraficoCategoriaTransacoes.vue';
import TabelaTransacoes from './components/TabelaTransacoes.vue';
import GastoMensal from './components/GastoMensal.vue';
import axios from 'axios';

var date = new Date(), y = date.getFullYear(), m = date.getMonth();
var firstDay = new Date(y, m-1, 0);
var lastDay = new Date(y, m+1, date.getDay());

export default {
  name: 'app',
  components: {
    GraficoTransacoes,
    GraficoCategoriaTransacoes,
    TabelaTransacoes,
    GastoMensal,
    Barra,
  },
  data() {
    return {
      //transacoes,
      transacoes: [],
      range: {
        start: firstDay, 
        end: lastDay, 
      },
      postURL: 'http://localhost:5000/send_transacoes',
    }
  },
  methods: {
    getMessage() {
      const path = 'http://localhost:5000/send_transacoes';
      axios.get(path)
        .then((res) => {
          this.transacoes = res.data.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getMessage();
  },
}
</script>

<style>

@import url('https://fonts.googleapis.com/css2?family=Goldman&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Arvo&display=swap');

#app {
  display: flex;
  background-color: #5abbbd;
  font-family: "Roboto";
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: white;
}

.container {
  padding-top: 156px;
}

.logo-and-wordmark {
  justify-content: center;
  margin-bottom: 30px;
  display: flex;
}

.logo {
  display: flex;
  margin-right: 10px;
}

.logo-img {
  align-self: flex-end;
}

.wordmark { 
  align-self: flex-end;
  display: flex;
  justify-content: flex-end;
}

.wordmark-text {
  font-size: 75px;
  line-height: 52px;
  height: 52px;
  font-family: 'Goldman';
  color: white;
}

.dashboard {
  padding-bottom: 38px;
  width: 100%;
}

.dashboard__summary {
  display: flex;
  justify-content: space-around;
  margin: 0.5rem 0;
  font-family: 'Roboto';
}
.scorecard__value {
  font-size: 1.5rem;
  font-weight: 700;
  font-family: 'Roboto';
  color: var(white);;
}
.scorecard__header {
  margin-top: 0.4rem;
}
.scorecard__subheader {
  font-size: 0.8rem;
}


</style>