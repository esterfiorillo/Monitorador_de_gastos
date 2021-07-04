<template>
  <zing-grid
    ref="myGrid"
    layout="row"
    pager
    page-size="5"
    page-size-options="5,10,20"
    control-bar="false"
    style="width: 100%;"
    height="241px"
    theme="Default"
    :data.prop="entries"
  >
    <zg-colgroup>
      <zg-column index="timestamp" header="Data" align="center" type="date"></zg-column>
      <zg-column index="descricao" header="Descrição" align="center" type="text"></zg-column>
      <zg-column index="categoria" header="Categoria" align="center" type="text"></zg-column>
      <zg-column index="valor" header="Valor" align="center" type="currency" type-currency="BRL"></zg-column>
    </zg-colgroup>
  </zing-grid>
</template>

<script>
export default {
  props: ['entries'],
}
</script>
<style>

zg-head-cell {
  background: white;
  color: #0080ab;
  font-size: 1rem;
}

zg-control-bar {
  display: none;
}
zg-caption {
color: #0080ab;
font-family: "Roboto";
font-weight: bold;
background: white;
padding-left: 0;
font-size: 1.4rem;
height: 54px;
text-align: left;

}
zing-grid {
  border: 0px;
}

zing-grid input[type="text"], zing-grid input[type="number"]{
  border-radius: 5px;
}

</style>