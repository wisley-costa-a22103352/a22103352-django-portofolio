function adicionar(valor) {
  var resultado = document.getElementById('resultado');
  resultado.value += valor;
}

function limpar() {
  var resultado = document.getElementById('resultado');
  resultado.value = '';
}

function calcular() {
  var resultado = document.getElementById('resultado');
  try {
    resultado.value = eval(resultado.value);
  } catch (error) {
    resultado.value = 'Erro';
  }
}

function sen() {
  var resultado = document.getElementById('resultado');
  resultado.value = Math.sin(eval(resultado.value));
}

function cos() {
  var resultado = document.getElementById('resultado');
  resultado.value = Math.cos(eval(resultado.value));
}

function tan() {
  var resultado = document.getElementById('resultado');
  resultado.value = Math.tan(eval(resultado.value));
}

function raiz() {
  var resultado = document.getElementById('resultado');
  resultado.value = Math.sqrt(eval(resultado.value));
}

function exponencial() {
  var resultado = document.getElementById('resultado');
  resultado.value = Math.pow(eval(resultado.value), 2);
}

function log() {
  var resultado = document.getElementById('resultado');
  resultado.value = Math.log10(eval(resultado.value));
}

function ajustarLargura() {
  var resultado = document.getElementById('resultado');
  resultado.style.width = ((resultado.value.length + 1) * 15) + 'px';
}