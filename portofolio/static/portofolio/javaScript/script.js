function adicionar(valor) {
  var resultado = document.getElementById('resultado');
  resultado.value += valor;
}

function limpar() {
  var resultado = document.getElementById('resultado');
  resultado.value = '';
}

function apagar() {
  var resultado = document.getElementById('resultado');
  resultado.value = resultado.value.slice(0, -1);
}

function calcular() {
  var resultado = document.getElementById('resultado');
  try {
    resultado.value = eval(resultado.value);
  } catch (error) {
    resultado.value = 'Erro';
  }
}
